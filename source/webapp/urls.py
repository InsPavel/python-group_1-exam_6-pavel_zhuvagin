from django.urls import path
from webapp.views import IndexListView

app_name = 'webapp'

urlpatterns = [
    path('', IndexListView.as_view(), name="index")
]