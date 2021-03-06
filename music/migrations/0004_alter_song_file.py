# Generated by Django 3.2.8 on 2021-10-05 20:57

from django.db import migrations, models
import music.models
import music.validators


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(null=True, upload_to=music.models.Song.song_directory_path, validators=[music.validators.validate_file_extension]),
        ),
    ]
