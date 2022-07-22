from statistics import mode
from unicodedata import category
from django.db import models
from django.urls import reverse

STATUS = {
    ('P','Planning Stage'),
    ('I','InProgress'),
    ('N','Not Started'),
    ('C','Completed'),
}


class Tags(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tags_detail', kwargs={'pk': self.id})    

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    tags = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    taggs = models.ManyToManyField(Tags)

    def  __str__(self):
        return self.name

    # This function gets the detail route with the current Ideas id.
    def get_absolute_url(self):
        return reverse('detail', kwargs={'idea_id': self.id})

class ProgressUpdate(models.Model):
    date = models.DateTimeField('Update on:')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.name}"

    class Meta:
        ordering = ['-date']