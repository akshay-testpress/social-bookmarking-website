from django.views import generic
import datetime
from django.db.models.functions import Concat
from pytz import timezone
from django.db.models import Value
from .models import MoviesMaster, MoviesGenres, MoviesStudios, MoviesDirectors
from django.contrib.auth.mixins import LoginRequiredMixin


class MoviesList(LoginRequiredMixin, generic.ListView):
    template_name = 'movies/moviesList.html'
    context_object_name = 'movielist'

    def get_queryset(self):
        return MoviesMaster.objects.filter(
            release_date__lte=datetime.datetime.now(timezone('UTC'))
        ).order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Movie List"
        context['page_heading'] = "Movies"
        return context


class MovieDetail(LoginRequiredMixin, generic.DetailView):
    model = MoviesMaster
    template_name = 'movies/moviedetail.html'
    context_object_name = 'moviedetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "movie"
        return context


class MovieGenreList(LoginRequiredMixin, generic.ListView):
    template_name = 'movies/genrelist.html'
    context_object_name = 'basic_list'

    def get_queryset(self):
        return MoviesGenres.objects.order_by('title')


class GenerMoviesList(LoginRequiredMixin, generic.ListView):
    template_name = 'movies/moviesList.html'
    context_object_name = 'movielist'

    def get_queryset(self):
        genre_id = self.kwargs['genre_id']
        return MoviesMaster.objects.filter(
            genre=genre_id,
            release_date__lte=datetime.datetime.now(timezone('UTC'))
        ).order_by('title')

    def get_context_data(self, **kwargs):
        genre_id = self.kwargs['genre_id']
        genre = MoviesGenres.objects.filter(pk=genre_id)
        context = super().get_context_data(**kwargs)
        context['title'] = "All genre movies"
        context['page_heading'] = str(genre[0].title)+" Movies"
        return context


class MovieStudioList(LoginRequiredMixin, generic.ListView):
    template_name = 'movies/studiolist.html'
    context_object_name = 'basic_list'

    def get_queryset(self):
        return MoviesStudios.objects.order_by('prefix', 'title')


class MovieStudioDetail(LoginRequiredMixin, generic.DetailView):
    model = MoviesStudios
    template_name = 'movies/studiodetail.html'
    context_object_name = 'basic_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "studio"
        return context


class MovieDirectorList(LoginRequiredMixin, generic.ListView):
    template_name = 'movies/directorlist.html'
    context_object_name = 'basic_list'

    def get_queryset(self):
        return MoviesDirectors.objects.annotate(
            title=Concat(
                'first_name',
                Value(' '),
                'last_name'
            )
        )


class MovieDirectorDetail(LoginRequiredMixin, generic.DetailView):
    model = MoviesDirectors
    template_name = 'movies/directordetail.html'
    context_object_name = 'basic_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Director"
        return context
