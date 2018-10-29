from django.views import generic
from . import models
from datetime import datetime
from pytz import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


class ArtistView(LoginRequiredMixin, generic.ListView):
    template_name = 'musics/artist_list.html'
    context_object_name = 'artist_list'
    # login_url="users:login"

    def get_queryset(self):
        return models.Artists.objects.order_by(
            'first_name',
            'middle_name',
            'last_name'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Artist"
        context['page_heading'] = "Artists"
        return context


class ArtistDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Artists
    template_name = 'musics/artist_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Artist"
        return context


class BandListView(LoginRequiredMixin, generic.ListView):
    template_name = 'musics/band_list.html'
    context_object_name = 'band_list'

    def get_queryset(self):
        return models.Bands.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Band"
        context['page_heading'] = "Bands"
        return context


class BandDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Bands
    template_name = 'musics/band_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Band"
        return context


class LabelListView(LoginRequiredMixin, generic.ListView):
    template_name = 'musics/label_list.html'
    context_object_name = 'label_list'

    def get_queryset(self):
        return models.LabelMaster.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Label"
        context['page_heading'] = "Labels"
        return context


class LabelDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.LabelMaster
    template_name = 'musics/label_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Label"
        return context


class AlbumListView(LoginRequiredMixin, generic.ListView):
    template_name = 'musics/album_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return models.Albums.objects.filter(release_date__lte=datetime.now(
            timezone('UTC'))
        ).order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Album"
        context['page_heading'] = "Albums"
        return context


class AlbumDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Albums
    template_name = 'musics/album_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        album_id = self.kwargs["pk"]
        artists_list = []
        objects = models.ArtistInAlbums.objects.only(
            "artist_id").filter(album_id=album_id)
        for ob in objects:
            artists_list.append(str(ob.artist_id))
        artists = ','.join(artists_list)

        context = super().get_context_data(**kwargs)
        context['title'] = "Album"
        context['artist_names'] = artists
        return context


class SongListView(LoginRequiredMixin, generic.ListView):
    template_name = 'musics/song_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return models.Musics.objects.filter(
            release_date__lte=datetime.now()
        ).order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Songs"
        context['page_heading'] = "All"
        return context


class SongDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Musics
    template_name = 'musics/song_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        song_id = self.kwargs["pk"]
        artists_list = []
        objects = models.ArtistInMusics.objects.only(
            "artist_id").filter(music_id=song_id)
        for ob in objects:
            artists_list.append(str(ob.artist_id))
        artists = ','.join(artists_list)

        context = super().get_context_data(**kwargs)
        context['title'] = "Song"
        context['artist_names'] = artists
        return context


class GenreListView(LoginRequiredMixin, generic.ListView):
    template_name = 'musics/genre_list.html'
    context_object_name = 'genre_list'

    def get_queryset(self):
        return models.MusicGenres.objects.order_by('title')


class GenreWiseSongView(LoginRequiredMixin, generic.ListView):
    model = models.Musics
    template_name = 'musics/song_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        genre_id = self.kwargs["genre_id"]
        return models.Musics.objects.filter(genre_id=genre_id,
                                            release_date__lte=datetime.now()
                                            ).order_by('title')

    def get_context_data(self, **kwargs):
        genre_id = self.kwargs["genre_id"]
        gener = models.MusicGenres.objects.filter(
            id=genre_id).order_by('title')

        context = super().get_context_data(**kwargs)
        context['title'] = "Song"
        context['page_heading'] = gener[0]
        return context


class AllSongsByArtist(LoginRequiredMixin, generic.ListView):
    template_name = "musics/song_list.html"
    context_object_name = "objects"
    # use through

    def get_queryset(self):
        artist_id = self.kwargs["artist_id"]
        return models.ArtistInMusics.objects.filter(artist_id=artist_id).all()


class AllSongsInAlbum(LoginRequiredMixin, generic.ListView):
    template_name = "musics/song_list.html"
    context_object_name = "objects"

    def get_queryset(self):
        album_id = self.kwargs["album_id"]
        return models.Musics.objects.filter(album_id=album_id,
                                            release_date__lte=datetime.now()
                                            )
