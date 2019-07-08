# Generated by Django 2.1.4 on 2019-01-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190107_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.CharField(max_length=200, verbose_name='О продукте'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Ид'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='uploads/products', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=8, verbose_name='Вес'),
        ),
    ]
