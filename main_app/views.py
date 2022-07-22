from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Idea, Tags
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
    id_list = idea.taggs.all().values_list('id')
    tags_idea_doesnt_have = Tags.objects.exclude(id__in=id_list)
    progressupdate_form = ProgressUpdateForm()
    return render(request, 'ideas/detail.html', {
        'idea': idea,
        'progressupdate_form': progressupdate_form,
        'tags': tags_idea_doesnt_have,
    })


class IdeaCreate(CreateView):
    model = Idea
    fields = ['name', 'category', 'description', 'status']


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


class TagsList(ListView):
    model = Tags


class TagsDetail(DetailView):
    model = Tags


class TagsCreate(CreateView):
    model = Tags
    fields = '__all__'


class TagsUpdate(UpdateView):
    model = Tags
    fields = ['name']


class TagsDelete(DeleteView):
    model = Tags
    success_url = '/tags/'


def assoc_tag(request, idea_id, tag_id):
    Idea.objects.get(id=idea_id).taggs.add(tag_id)
    return redirect('detail', idea_id=idea_id)


def unassoc_tag(request, idea_id, tag_id):
    Idea.objects.get(id=idea_id).taggs.remove(tag_id)
    return redirect('detail', idea_id=idea_id)
