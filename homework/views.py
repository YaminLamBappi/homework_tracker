from django.shortcuts import render, redirect, get_object_or_404
from .forms import HomeworkForm, TagForm, NotesForm
from django.utils import timezone
from .models import Homework, Tag, Notes
from django.contrib.auth.decorators import login_required

from datetime import date

@login_required
def homework_list(request):
    all_tags = Tag.objects.all()
    homework_list = Homework.objects.all()
    tag_filter = request.POST.get('tag_filter')

    if tag_filter:
        homework_list = homework_list.filter(tags__tag_name=tag_filter)

    today = date.today()

    return render(request, 'homework_list.html', {'homework_list': homework_list, 'all_tags': all_tags, 'today': today})

@login_required
def view_notes(request):
    notes = Notes.objects.all()
    subjects = set(notes.values_list('subject', flat=True))
    
    if request.method == "POST":
        subject_filter = request.POST.get('subject')
        if subject_filter:
            notes = notes.filter(subject=subject_filter)
    
    return render(request, 'viewnote.html', {'notes': notes, 'subjects': subjects})

@login_required
def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.user = request.user 
            form.save()
            return redirect('homework_list')
    else:
        form = HomeworkForm()
    return render(request, 'homework.html', {'form': form})


@login_required
def edit_homework(request, homework_id):
    homework = Homework.objects.get(id=homework_id)
    
    editing_available = True

    if homework.due_date < timezone.now().date():
        editing_available = False

    if request.method == "POST":
        form = HomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homework_list')
    else:
        form = HomeworkForm(instance=homework)
    return render(request, 'edit_homework.html', {'form': form, 'editing_available': editing_available})

@login_required
def edit_note(request, note_id):
    note = Notes.objects.get(id=note_id)
    
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('viewnote')
    else:
        form = HomeworkForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})



@login_required
def delete_homework(request, homework_id):
    homework = Homework.objects.get(id=homework_id)
    homework.delete()
    return redirect('homework_list')


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homework_list')
    else:
        form = TagForm()  

    return render(request, "addtag.html", {'form': form})




@login_required
def add_notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST,request.FILES)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            form.save()
            return redirect('viewnote')
    else:
        form = NotesForm()
    return render(request, "addnotes.html", {'form':form})    