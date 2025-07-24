from rest_framework import viewsets, permissions
from .models import AnimeSeason, Episode
from .serializers import AnimeSeasonSerializer, EpisodeSerializer

class AnimeSeasonViewSet(viewsets.ModelViewSet):
    queryset = AnimeSeason.objects.all()
    serializer_class = AnimeSeasonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]