from django.shortcuts import render, redirect
from .forms import HomeworkForm
from django.utils import timezone
from .models import Homework, Tag
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
def delete_homework(request, homework_id):
    homework = Homework.objects.get(id=homework_id)
    homework.delete()
    return redirect('homework_list')