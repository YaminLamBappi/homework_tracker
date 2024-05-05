
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('', views.user_login, name="user_login" ),
    path('', include("homework.urls")),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),

]
