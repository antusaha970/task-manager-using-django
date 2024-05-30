from django.shortcuts import render, redirect
from .form import CategoryForm
# Create your views here.


def add_category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = CategoryForm()
    return render(request, 'category/addCategory.html', {'form': form})
