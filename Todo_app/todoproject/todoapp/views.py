from django.shortcuts import render, redirect
from todoapp.models import Task

def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        ins = Task(title=title, description=desc)
        ins.save()
        context = {'success': True}
        return render(request, 'home.html', context)

    return render(request, 'home.html')

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def mark_completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('tasks')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('tasks')