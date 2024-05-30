from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_category_form, name="add_category"),
]
