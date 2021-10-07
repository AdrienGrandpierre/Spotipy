from django.contrib.auth.models import User, Group
from rest_framework import serializers

from music.models import Artist, Song, Genre


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ArtistSerializer(serializers.ModelSerializer):
    genre_name = serializers.ReadOnlyField(source='genre.name')
    # genre_name = serializers.CharField(source='genre.name')

    class Meta:
        model = Artist
        fields = ['id', 'genre_name','name', 'genre']
        # fields = ['name', 'genre_name']


class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.ReadOnlyField(source='artist.name')

    class Meta:
        model = Song
        fields = ['id', 'artist', 'artist_name',  'name', 'file', 'duration', 'created_at', 'status']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']
