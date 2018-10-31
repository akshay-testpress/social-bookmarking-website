from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("account/", include('accounts.urls')),
    path("movies/", include('movies.urls')),
    path("musics/", include('musics.urls')),
    path("users/", include('users.urls')),
    path("places/", include('places.urls')),
    path("events/", include('events.urls')),
]
