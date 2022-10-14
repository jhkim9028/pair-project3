from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie_name = models.TextField()
    grade = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)