from django.urls import path
from webapp.views import IndexListView, PostListView

app_name = 'webapp'

urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('post', PostListView.as_view(), name="post_list")
]