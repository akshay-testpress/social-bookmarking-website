from django.urls import path
from . import views

app_name = 'places'
urlpatterns = [
    path('', views.PlaceView.as_view(), name="allPlaces"),
    path("<slug>/<int:pk>/", views.PlaceDetailView.as_view(),
         name="placeDetail"),
    path('add/', views.insert_places, name="add"),
]
