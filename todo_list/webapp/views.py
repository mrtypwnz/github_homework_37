from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': tasks
    })

def edit_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method =='GET':
        return render(request, 'edit_view.html', context={
            'task':task
        })

    elif request.method == 'POST':
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()
        return redirect('index')

def task_done(request, task_pk, status):
    task = get_object_or_404(Task, pk=task_pk)
    task.status = status
    task.save()
    return redirect('index')

def create_view(request):
    Task.objects.create(
        name=request.POST.get('name'),
        due_date=request.POST.get('due_date')
    )
    return redirect('index')


def delete_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('index')
