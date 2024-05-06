from django.contrib import admin
from .models import Notes


class NotesMyAdmin(admin.ModelAdmin):
    list_display = ['note','subject','file', 'date']
    
admin.site.register(Notes,NotesMyAdmin)
