from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Idea
from .forms import ProgressUpdateForm

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
    progressupdate_form = ProgressUpdateForm()
    return render(request, 'ideas/detail.html', { 'idea': idea, 'progressupdate_form': progressupdate_form})

class IdeaCreate(CreateView):
    model = Idea
    fields = '__all__'
class IdeaUpdate(UpdateView):
    model = Idea
    fields = '__all__'
class IdeaDelete(DeleteView):
    model = Idea
    success_url = '/ideas/'

def add_progressupdate(request, idea_id):
    form = ProgressUpdateForm(request.POST)
    if form.is_valid():
        new_progressupdate = form.save(commit=False)
        new_progressupdate.idea_id = idea_id
        new_progressupdate.save()
    return redirect('detail', idea_id=idea_id)