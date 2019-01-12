from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, View
from webapp.models import UserInfo, Post
from webapp.forms import PostForm

class IndexListView(ListView):
    model = UserInfo
    template_name = 'index.html'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-public_data')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'


