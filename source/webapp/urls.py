from django.urls import path
from webapp.views import IndexListView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('post', PostListView.as_view(), name="post_list"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('post/create', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post_delete"),
]