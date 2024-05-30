from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        help_texts = {
            'category': "Available categories",
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter task description'}),
        }
