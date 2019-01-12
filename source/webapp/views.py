from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import UserInfo, Post

class IndexListView(ListView):
    model = UserInfo
    template_name = 'index.html'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'