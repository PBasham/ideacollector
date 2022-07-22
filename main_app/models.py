from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    tags = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def  __str__(self):
        return self.name

    # This function gets the detail route with the current Ideas id.
    def get_absolute_url(self):
        return reverse('detail', kwargs={'idea_id': self.id})