from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    url = models.URLField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)