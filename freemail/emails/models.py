from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Members(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=50)
    code=models.CharField(max_length=100)
    
class Ymail(models.Model):
     receiver=models.CharField(max_length=100)
     msg=models.TextField()

