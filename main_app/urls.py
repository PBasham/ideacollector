from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ideas/', views.ideas_index, name='index'),
    path('ideas/<int:idea_id>/', views.ideas_detail, name='detail'),
    path('ideas/create/', views.IdeaCreate.as_view(), name='idea_create'),
    path('ideas/<int:pk>/update/', views.IdeaUpdate.as_view(), name='ideas_update'),
    path('ideas/<int:pk>/delete/', views.IdeaDelete.as_view(), name='ideas_delete'),
]