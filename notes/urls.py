
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('viewnotes/', views.view_notes, name="viewnote"),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('addnotes/', views.add_notes, name="addnotes"),
    path('delete_notes/<int:note_id>/', views.delete_notes, name="delete_notes")
]
