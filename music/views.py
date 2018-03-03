from django.views import generic
from .models import Album, Song
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class Index(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class Details(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

    def get_object(self):
        return get_object_or_404(Album.objects.filter(title=self.kwargs['albumName']))


def NewSong(request, albumName):
    album = get_object_or_404(Album.objects.filter(title=albumName))
    songTitle = request.POST['title']
    album.song_set.create(title=songTitle)

    return HttpResponseRedirect(reverse('details', args=(albumName,)))


def AddAlbum(request):
    return render(request, 'music/addalbum.html')


def NewAlbum(request):
    title = request.POST['title']
    artist = request.POST['artist']
    genre = request.POST['genre']
    logo = request.POST['logo']

    newAlbum = Album(title=title, artist=artist, genre=genre, logo=logo)
    newAlbum.save()
    return HttpResponseRedirect(reverse('details', args=(title,)))


def RemoveSong(request, albumName, songTitle):
    album = Album.objects.get(title=albumName)
    song = album.song_set.filter(title=songTitle)
    song.delete()
    return HttpResponseRedirect(reverse('details', args=(albumName,)))


def FavoriteSong(request, albumTitle, songTitle, urlRedirect):
    album = Album.objects.get(title=albumTitle)
    song = album.song_set.get(title=songTitle)
    song.favorite = not song.favorite
    song.save()

    if urlRedirect == 'favorites':
        return HttpResponseRedirect(reverse(urlRedirect))
    else:
        return HttpResponseRedirect(reverse(urlRedirect, args=(albumTitle,)))


class Favorites(generic.ListView):
    template_name = 'music/favorites.html'

    def get_queryset(self):
        return Song.objects.filter(favorite=True)
