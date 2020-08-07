from django.shortcuts import render
from .models import Meme


def home(request):

    info = {
        'memes': Meme.objects.all()
    }

    return render(request, 'meme/home.html', info)

def about(request):
    return HttpResponse('<h1> About Page </h1>')