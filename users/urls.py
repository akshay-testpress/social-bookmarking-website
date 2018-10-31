from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logOut, name="logout"),
    # path('places/', views.home, name="place")
]
