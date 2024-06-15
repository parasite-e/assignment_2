from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm

def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, 'tasks/show_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    task.delete()
    return redirect('show_tasks')

def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})
