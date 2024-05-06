from django.contrib import admin
from .models import Tag, Homework


class TagMyAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

class HomeworkMyAdmin(admin.ModelAdmin):
    list_display = ['homework_task', 'sub_headline', 'due_date']


    
admin.site.register(Tag, TagMyAdmin)
admin.site.register(Homework,HomeworkMyAdmin)