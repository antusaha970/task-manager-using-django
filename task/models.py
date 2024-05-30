from django.db import models
from category.models import Category
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=300, verbose_name="Task Title")
    description = models.TextField(verbose_name="Task Description")
    is_completed = models.BooleanField(
        default=False, verbose_name="Is task completed?")
    task_assigned = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name="Task Category")

    def __str__(self) -> str:
        return self.title
