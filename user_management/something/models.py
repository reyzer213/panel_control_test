from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, default='user')

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name