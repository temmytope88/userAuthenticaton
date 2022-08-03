import email
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class MyUsers(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=20, default="value")