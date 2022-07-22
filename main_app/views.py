from django.shortcuts import render
from .models import Idea

# Create your views here.
from django.http import HttpResponse

# Defind the home view
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def ideas_index(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/index.html', {'ideas': ideas})
def ideas_detail(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    return render(request, 'ideas/detail.html', { 'idea': idea})