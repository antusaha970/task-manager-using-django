from django.shortcuts import render, redirect
from .form import TaskForm

# Create your views here.


def homePage(request):
    return render(request, 'task/homePage.html')


def addTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = TaskForm()
    return render(request, 'task/addTask.html', {'form': form})
