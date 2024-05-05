
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homework, name = "homework"),
    path('list/', views.homework_list, name="homework_list"),
    path('addtag/', views.add_tag, name="addtag"),
    path('homework/<int:homework_id>/edit/', views.edit_homework, name='edit_homework'),
    path('delete_homework/<int:homework_id>/', views.delete_homework, name='delete_homework'),
]
