from django.db import models
from user.models import User

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
