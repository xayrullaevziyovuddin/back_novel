from django.contrib import admin
from .models import AnimeSeason, Episode

@admin.register(AnimeSeason)
class AnimeSeasonAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'created_at']
    search_fields = ['title']

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'season', 'episode_number', 'created_at']
    list_filter = ['season', 'created_at']
    search_fields = ['title']