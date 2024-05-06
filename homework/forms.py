from django import forms
from .models import Homework, Tag, Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note','subject','file', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['homework_task', 'sub_headline', 'due_date', 'tags']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
class TagForm(forms.ModelForm):
    class Meta: 
        model = Tag
        fields = ['tag_name',]