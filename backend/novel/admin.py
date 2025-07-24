from django.contrib import admin
from .models import Volume, Chapter

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'volume', 'order', 'created_at']
    list_filter = ['volume', 'created_at']
    search_fields = ['title']