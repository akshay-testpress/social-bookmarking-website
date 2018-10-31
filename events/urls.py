from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.EventsUpcomingListView.as_view(), name='allevents'),
    path('foraday/', views.EventsInOneDayListView.as_view(), name='foraday'),
    path('foramonth/', views.EventsInOneMonthListView.as_view(),
         name='foramonth'),
    path('foryear/', views.EventsInOneYearListView.as_view(), name='forayear'),
    path('<slug>/<int:pk>/', views.EventDetailView.as_view(),
         name='detail'),
    path('add/', views.event_add, name='add'),
]
