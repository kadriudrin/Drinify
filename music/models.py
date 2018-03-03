from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
