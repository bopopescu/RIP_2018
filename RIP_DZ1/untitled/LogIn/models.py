from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    about = models.CharField(max_length=254,blank=True, null=True, verbose_name='О профиле')
    avatar = models.ImageField(null=True,blank=True, upload_to='uploads/avatars', verbose_name='Аватар')
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
