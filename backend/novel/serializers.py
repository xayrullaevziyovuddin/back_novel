from rest_framework import serializers
from .models import Volume, Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'audio_file', 'illustration', 'content', 'order', 'created_at']


class VolumeSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Volume
        fields = ['id', 'title', 'description', 'created_at', 'chapters']