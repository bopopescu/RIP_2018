from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='Ид')
    name = models.CharField(max_length=120,null=False, verbose_name='Имя')
    about = models.CharField(max_length=200, verbose_name='О продукте')
    price = models.CharField(max_length=8, verbose_name='Цена')
    weight = models.CharField(max_length=8, verbose_name='Вес')
    picture = models.ImageField(null=False, upload_to='uploads/products', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

