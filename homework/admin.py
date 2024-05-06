from django.contrib import admin
from .models import Tag, Homework, Notes


class TagMyAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

class HomeworkMyAdmin(admin.ModelAdmin):
    list_display = ['homework_task', 'sub_headline', 'due_date']


class NotesMyAdmin(admin.ModelAdmin):
    list_display = ['note','subject','file', 'date']
    
admin.site.register(Notes,NotesMyAdmin)
admin.site.register(Tag, TagMyAdmin)
admin.site.register(Homework,HomeworkMyAdmin)