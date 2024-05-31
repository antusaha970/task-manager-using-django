from django.shortcuts import render, redirect
from .form import TaskForm
from .models import Task

# Create your views here.


def homePage(request):
    tasks = Task.objects.all()
    return render(request, 'task/homePage.html', {'tasks': tasks})


def addTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = TaskForm()
    return render(request, 'task/addTask.html', {'form': form})


def editTask(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("homePage")

    return render(request, 'task/addTask.html', {'form': form})


def deleteTask(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect("homePage")
