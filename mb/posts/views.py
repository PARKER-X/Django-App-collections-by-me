from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'all_posts_list'