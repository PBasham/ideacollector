from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ideas/', views.ideas_index, name='index'),
    path('ideas/<int:idea_id>/', views.ideas_detail, name='detail'),
]