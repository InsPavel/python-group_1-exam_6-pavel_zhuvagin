from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserInfo(models.Model):
    name = models.OneToOneField(User, on_delete=True, related_name='user', verbose_name='Пользователяь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    friends = models.ManyToManyField(User, blank=True, related_name='friend', verbose_name='Друзья')
    avatar = models.ImageField(null=True, blank=True, verbose_name='Фотография')

class Post(models.Model):
    author = models.ForeignKey(User, related_name='author', verbose_name='Автор', on_delete=models.PROTECT)
    title = models.TextField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    public_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s. %s: %s' % (self.pk, self.author, self.title)
