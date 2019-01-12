from django import forms
from webapp.models import Post, UserInfo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['phone', 'avatar']
