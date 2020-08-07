from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Memendr'),
    path('about/', views.about, name='about'),
]