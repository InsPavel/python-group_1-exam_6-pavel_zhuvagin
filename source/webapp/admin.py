from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from webapp.models import UserInfo, Post

class UserInfoInLine(admin.StackedInline):
    model = UserInfo
    fields = ['phone', 'friends', 'avatar']

class UserInfoAdmin(UserAdmin):
    inlines = [UserInfoInLine]

admin.site.unregister(User)
admin.site.register(User, UserInfoAdmin)
admin.site.register(Post)
