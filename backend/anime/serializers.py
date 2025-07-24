from rest_framework import serializers
from .models import AnimeSeason, Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'title', 'episode_number', 'video_file', 'description', 'created_at']


class AnimeSeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = AnimeSeason
        fields = ['id', 'title', 'description', 'release_year', 'created_at', 'episodes']