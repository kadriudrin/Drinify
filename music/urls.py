from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # /AddAlbum/
    path('AddAlbum/', views.AddAlbum, name='addAlbum'),
    # /AddAlbum/NewAlbum/
    path('AddAlbum/NewAlbum/', views.NewAlbum, name='newAlbum'),
    # /Favorites/
    path('Favorites/', views.Favorites.as_view(), name='favorites'),
    # /<Album Name>/
    path('<str:albumName>/', views.Details.as_view(), name='details'),
    # /<Album Name>/<Song Name>/RemoveSong/
    path('<str:albumName>/<str:songTitle>/RemoveSong', views.RemoveSong, name='removeSong'),
    # /<Album Name>/NewSong/
    path('<str:albumName>/NewSong/', views.NewSong, name='newSong'),
    # /<Album Name>/<Song Name>/<Url Redirect>
    path('<str:albumTitle>/<str:songTitle>/<str:urlRedirect>/', views.FavoriteSong, name='favoriteSong'),
]
