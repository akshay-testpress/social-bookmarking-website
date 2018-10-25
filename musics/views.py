from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.
class ArtistView(generic.ListView):
    template_name = 'musics/artist_list.html'
    context_object_name = 'artist_list'

    def get_queryset(self):
        return  models.Artists.objects.order_by('first_name','middle_name','last_name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Artist"
        context['page_heading'] = "Artists"
        return context

class ArtistDetailView(generic.DetailView):
    model = models.Artists
    template_name = 'musics/artist_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Artist"
        return context

class BandListView(generic.ListView):
    template_name = 'musics/band_list.html'
    context_object_name = 'band_list'

    def get_queryset(self):
        return  models.Bands.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Band"
        context['page_heading'] = "Bands"
        return context

class BandDetailView(generic.DetailView):
    model = models.Bands
    template_name = 'musics/band_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Band"
        return context

class LabelListView(generic.ListView):
    template_name = 'musics/label_list.html'
    context_object_name = 'label_list'

    def get_queryset(self):
        return  models.LabelMaster.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Label"
        context['page_heading'] = "Labels"
        return context

class LabelDetailView(generic.DetailView):
    model = models.LabelMaster
    template_name = 'musics/label_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Label"
        return context

class AlbumListView(generic.ListView):
    template_name = 'musics/album_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return  models.Albums.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Album"
        context['page_heading'] = "Albums"
        return context

class AlbumDetailView(generic.DetailView):
    model = models.Albums
    template_name = 'musics/album_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        album_id = self.kwargs["pk"]
        artists_list = []
        objects = models.ArtistInAlbums.objects.only("artist_id").filter(album_id=album_id)
        for ob in objects:
            artists_list.append(str(ob.artist_id))
        artists = ','.join(artists_list)

        context = super().get_context_data(**kwargs)
        context['title'] = "Album"
        context['artist_names'] = artists
        return context

class SongListView(generic.ListView):
    template_name = 'musics/song_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return  models.Musics.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Songs"
        context['page_heading'] = "All"
        return context

class SongDetailView(generic.DetailView):
    model = models.Musics
    template_name = 'musics/song_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        song_id = self.kwargs["pk"]
        artists_list = []
        objects = models.ArtistInMusics.objects.only("artist_id").filter(music_id=song_id)
        for ob in objects:
            artists_list.append(str(ob.artist_id))
        artists = ','.join(artists_list)

        context = super().get_context_data(**kwargs)
        context['title'] = "Song"
        context['artist_names'] = artists
        return context

class GenreListView(generic.ListView):
    template_name = 'musics/genre_list.html'
    context_object_name = 'genre_list'

    def get_queryset(self):
        return  models.MusicGenres.objects.order_by('title')

class GenreWiseSongView(generic.ListView):
    model = models.Musics
    template_name = 'musics/song_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        genre_id = self.kwargs["genre_id"]
        return  models.Musics.objects.filter(genre_id=genre_id).order_by('title')

    def get_context_data(self, **kwargs):
        genre_id = self.kwargs["genre_id"]
        gener = models.MusicGenres.objects.filter(id=genre_id).order_by('title')

        context = super().get_context_data(**kwargs)
        context['title'] = "Song"
        context['page_heading'] = gener[0]
        return context

class AllSongsByArtist(generic.ListView):
    template_name="musics/song_list.html"
    context_object_name = "objects"

    def get_queryset(self):
        artist_id = self.kwargs["artist_id"]
        return models.Musics.objects.raw('''
                                    Select s.*
                                    FROM 
                                        musics_musics AS s
                                        INNER JOIN musics_artistinmusics AS am ON s.id = am.music_id_id
                                    WHERE
                                        am.artist_id_id=%s''',
                                        [artist_id]
                                    )

class AllSongsInAlbum(generic.ListView):
    template_name="musics/song_list.html"
    context_object_name = "objects"

    def get_queryset(self):
        album_id = self.kwargs["album_id"]
        return models.Musics.objects.filter(album_id=album_id)
