from django.shortcuts import render, redirect
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Meme




def home(request):
    index = random.randrange(1, (len(Meme.objects.all())))
    print(index)
    info = {
        'meme': Meme.objects.get(pk=index)
    }
    return render(request, 'meme/home.html', info)

def like(request, pk):
    liked = Meme.objects.get(pk=pk)
    print(liked)
    liked.likes += 1
    liked.save()
    return redirect('Memendr')

def dislike(request, pk):
    disliked = Meme.objects.get(pk=pk)
    print(disliked)
    disliked.dislikes += 1
    disliked.save()
    return redirect('Memendr')


class MemeListView(ListView):
    model = Meme
    template_name = 'meme/home.html'
    context_object_name = 'memes'

class MemeDetailView(DetailView):
    model = Meme

class MemeCreateView(LoginRequiredMixin, CreateView):
    model = Meme
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class MemeUpdateView(UpdateView):
    model = Meme
    fields = ['title', 'image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

