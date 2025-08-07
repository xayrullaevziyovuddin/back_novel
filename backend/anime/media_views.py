import os
import re
import mimetypes
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse, Http404
from django.views import View
from django.conf import settings

range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)

class RangeFileWrapper(object):
    def __init__(self, filelike, blksize=8192, offset=0, length=None):
        self.filelike = filelike
        self.filelike.seek(offset, os.SEEK_SET)
        self.remaining = length
        self.blksize = blksize

    def __iter__(self):
        return self

    def __next__(self):
        if self.remaining is None:
            # If remaining is None, we're reading the entire file.
            data = self.filelike.read(self.blksize)
            if data:
                return data
            raise StopIteration()
        else:
            if self.remaining <= 0:
                raise StopIteration()
            data = self.filelike.read(min(self.remaining, self.blksize))
            if not data:
                raise StopIteration()
            self.remaining -= len(data)
            return data

    next = __next__


def range_file_response(request, file_path, content_type):
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = range_re.match(range_header)
    size = os.path.getsize(file_path)

    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = int(last_byte) if last_byte else size - 1
        if last_byte >= size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(RangeFileWrapper(open(file_path, 'rb'), offset=first_byte, length=length), status=206, content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        resp = StreamingHttpResponse(FileWrapper(open(file_path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)

    resp['Accept-Ranges'] = 'bytes'
    return resp

class ServeMediaView(View):
    def get(self, request, path):
        # Construct the full path to the media file
        full_path = os.path.join(settings.MEDIA_ROOT, path)

        # Check if the file exists and is a file
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            raise Http404("File not found")

        # Guess the content type
        content_type, encoding = mimetypes.guess_type(full_path)
        content_type = content_type or 'application/octet-stream'

        # Create a streaming response that supports range requests
        return range_file_response(request, full_path, content_type)
