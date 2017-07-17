from django.db import models


class Music(models.Model):
    name_music = models.CharField(max_length=100)
    name_singer = models.CharField(max_length=100)
    file_music = models.FileField()
    name_album = models.CharField(max_length=100)
    date_released = models.DateField(auto_now_add=True)
    tag_weather = models.CharField(max_length=1000)


class Musics(models.Model):
    music_info =