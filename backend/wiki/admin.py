from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias', 'created_at']
    search_fields = ['name', 'alias']