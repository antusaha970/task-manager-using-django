from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(
        max_length=255, error_messages="Category is required and must be under 255 characters", unique=True)

    def __str__(self) -> str:
        return self.category_name
