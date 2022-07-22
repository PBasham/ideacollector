from unicodedata import category
from django.db import models

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    tags = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def  __str__(self):
        return self.name