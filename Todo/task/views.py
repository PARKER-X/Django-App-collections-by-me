from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy


# Create your views here.
# def index(request):
#     return render(request, 'task/index.html')

class PostListView(ListView):
    model = Post
    template_name = "task/index.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "task/detail.html"
    fields='__all__'

class PostCreateView(CreateView):
    model = Post
    template_name = "task/create.html"
    fields='__all__'

class PostDeleteView(DeleteView):
    model = Post
    template_name = "task/delete.html"
    success_url = reverse_lazy('index')

class PostUpdateView(UpdateView):
    model = Post
    template_name = "task/update.html"
    fields='__all__'



    


