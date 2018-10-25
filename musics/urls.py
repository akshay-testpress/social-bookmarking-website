from django.urls import path
from . import views 

app_name="musics"
urlpatterns = [
    path("artists/", views.ArtistView.as_view(), name="artistlist"),
    path("artists/<int:pk>/", views.ArtistDetailView.as_view(), name="artistdetail"),

    path("bands/", views.BandListView.as_view(), name="bandlist"),
    path("bands/<int:pk>/", views.BandDetailView.as_view(), name="banddetail"),

    path("labels/", views.LabelListView.as_view(), name="labellist"),
    path("labels/<int:pk>/", views.LabelDetailView.as_view(), name="labeldetail"),

    path("albums/", views.AlbumListView.as_view(), name="albumlist"),
    path("albums/<int:pk>/", views.AlbumDetailView.as_view(), name="albumdetail"),

    path("songs/", views.SongListView.as_view(), name="songlist"),
    path("songs/<int:pk>/", views.SongDetailView.as_view(), name="songdetail"),

    path("genre/", views.GenreListView.as_view(), name="genrelist"),
    path("genre/<int:genre_id>/", views.GenreWiseSongView.as_view(), name="genredetail"),

    path("artistsong/<int:artist_id>/", views.AllSongsByArtist.as_view(), name="artistsong"),

    path("albumsong/<int:album_id>/", views.AllSongsInAlbum.as_view(), name="albumsong"),
]
