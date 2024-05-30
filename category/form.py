from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        help_texts = {
            'category_name': "Add an unique category name",
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder': 'Enter category name'})
        }
