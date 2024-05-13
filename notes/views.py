from django.shortcuts import render, redirect
from .forms import NotesForm
from .models import Notes
from django.contrib.auth.decorators import login_required



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
def edit_note(request, note_id):
    note = Notes.objects.get(id=note_id)
    
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('viewnote')
    else:
        form = NotesForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})




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

@login_required
def delete_notes(request, note_id):
    note = Notes.objects.get(id = note_id)
    note.delete()
    return redirect('viewnote')