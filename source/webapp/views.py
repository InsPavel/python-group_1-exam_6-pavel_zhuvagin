from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import UserInfo, Post
from webapp.forms import PostForm, UpdatePostForm, UpdateUserForm
from django.urls import reverse_lazy

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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s' % reverse('accounts:login'))
        return super().dispatch(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'post_update.html'

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        object = super(PostUpdateView, self).get_object()
        if object.author != self.request.user:
            return redirect('%s' % reverse('accounts:login'))
        return super().dispatch(request, *args, **kwargs)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('webapp:post_list')

    def dispatch(self, request, *args, **kwargs):
        object = super(PostDeleteView, self).get_object()
        if object.author != self.request.user:
            return redirect('%s' % reverse('accounts:login'))
        return super().dispatch(request, *args, **kwargs)

class UserInfoListView(ListView):
    model = UserInfo
    template_name = 'userinfo_list.html'

class UserInfoDetailView(DetailView):
    model = UserInfo
    template_name = 'userinfo_detail.html'

class UserUpdateView(UpdateView):
    model = UserInfo
    form_class = UpdateUserForm
    template_name = 'personal_update.html'

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        object = super(UserUpdateView, self).get_object()
        if object.name != self.request.user:
            return redirect('%s' % reverse('accounts:login'))
        return super().dispatch(request, *args, **kwargs)

