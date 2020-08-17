from django.urls import path
from .views import (
    MemeListView,
    MemeDetailView,
    MemeCreateView,
    MemeUpdateView
)
from . import views

urlpatterns = [
    path('', views.home, name='Memendr'),
    path('meme/<int:pk>/', MemeDetailView.as_view(), name='meme-detail'),
    path('meme/<int:pk>/like', views.like, name='meme-like'),
    path('meme/<int:pk>/dislike', views.dislike, name='meme-dislike'),
    path('meme/new/', MemeCreateView.as_view(), name='meme-create'),
    path('meme/<int:pk>/update', MemeUpdateView.as_view(), name='meme-update'),
    path('meme/show', MemeListView.as_view(), name="meme-show")
]