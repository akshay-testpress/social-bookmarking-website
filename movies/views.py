from django.shortcuts import render
from django.views import generic
from django.db import connection
from django.db.models.functions import Concat
from django.db.models import Value
from .models import MoviesMaster,MoviesGenres,MoviesStudios,MoviesDirectors

# Create your views here.
class MoviesList(generic.ListView):
    template_name='movies/moviesList.html'
    context_object_name = 'movielist'

    def get_queryset(self):
        return MoviesMaster.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Movie List"
        context['page_heading'] = "Movies"
        return context

class MovieDetail(generic.DetailView):
    model = MoviesMaster
    template_name='movies/moviedetail.html'
    context_object_name = 'moviedetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "movie"
        return context

class MovieGenreList(generic.ListView):
    template_name = 'movies/genrelist.html'
    context_object_name = 'basic_list'

    def get_queryset(self):
        return MoviesGenres.objects.order_by('title')

class GenerMoviesList(generic.ListView):
    template_name='movies/moviesList.html'
    context_object_name = 'movielist'

    def get_queryset(self):
        genre_id = self.kwargs['genre_id']
        return MoviesMaster.objects.filter(genre=genre_id).order_by('title')
        
    def get_context_data(self, **kwargs):
        genre_id = self.kwargs['genre_id']
        genre = MoviesGenres.objects.filter(pk=genre_id)
        context = super().get_context_data(**kwargs)
        context['title'] = "All genre movies"
        context['page_heading'] = str(genre[0].title)+" Movies"
        return context

class MovieStudioList(generic.ListView):
    template_name = 'movies/studiolist.html'
    context_object_name = 'basic_list'

    def get_queryset(self):
        return MoviesStudios.objects.order_by('prefix','title')

class MovieStudioDetail(generic.DetailView):
    model = MoviesStudios
    template_name='movies/studiodetail.html'
    context_object_name = 'basic_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "studio"
        return context

class MovieDirectorList(generic.ListView):
    template_name = 'movies/directorlist.html'
    context_object_name = 'basic_list'

    def get_queryset(self):
        return MoviesDirectors.objects.annotate(title=Concat('first_name',Value(' '),'last_name'))

class MovieDirectorDetail(generic.DetailView):
    model = MoviesDirectors
    template_name='movies/directordetail.html'
    context_object_name = 'basic_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Director"
        return context