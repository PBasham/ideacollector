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
    path('ideas/<int:idea_id>/add_progressupdate/', views.add_progressupdate, name='add_progressupdate'),
    path('ideas/<int:idea_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('tags/', views.TagsList.as_view(), name='tags_index'),
    path('toys/<int:pk>/', views.TagsDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagsCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.TagsUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.TagsDelete.as_view(), name='tags_delete'),
]