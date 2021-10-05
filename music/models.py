from enum import Enum

from django.db import models

# Create your models here.
from music.validators import validate_file_extension


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): return self.name


class Artist(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

    def __str__(self): return self.name


class Song(models.Model):
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_PRIVATE = 'private'

    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Brouillon'),
        (STATUS_PUBLISHED, 'Publié'),
        (STATUS_PRIVATE, 'Privé'),
    )

    def song_directory_path(self, filename):
        return 'songs/{0}/{1}'.format(self.artist.name, filename)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to=song_directory_path, null=True, validators=[validate_file_extension])
    duration = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_DRAFT)

    def __str__(self): return self.name
