from django.contrib import admin

# Register your models here.
from music.models import Artist, Song, Genre


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist', 'duration', 'created_at', 'status', 'file')
    list_filter = ('status', 'artist__name')
    search_fields = ['name']
    autocomplete_fields = ['artist']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre')
    list_filter = ('genre__name',)
    search_fields = ['name']
    autocomplete_fields = ['genre']



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
