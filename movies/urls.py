from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('', views.MoviesList.as_view(), name='movielist'),
    path('detail/<int:pk>/', views.MovieDetail.as_view(), name='moviedetail'),

    path('genre/', views.MovieGenreList.as_view(), name="genrelist"),
    path('genre-movies/<int:genre_id>',
         views.GenerMoviesList.as_view(), name="genremovie"),

    path('studio/', views.MovieStudioList.as_view(), name="studiolist"),
    path('studio/<int:pk>/',
         views.MovieStudioDetail.as_view(), name="studiodetail"),

    path('directors/', views.MovieDirectorList.as_view(), name="directorlist"),
    path('directors/<int:pk>/', views.MovieDirectorDetail.as_view(),
         name="directordetail"),

]
