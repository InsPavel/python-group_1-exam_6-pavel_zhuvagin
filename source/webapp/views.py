from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from webapp.models import UserInfo, Post
from webapp.forms import PostForm, UpdatePostForm

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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'post_update.html'

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})
