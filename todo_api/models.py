from django.db import models

# Create your models here.


class Todo(models.Model):
    todo = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
