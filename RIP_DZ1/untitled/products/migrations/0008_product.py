# Generated by Django 2.1.4 on 2019-01-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('picture', models.ImageField(upload_to='uploads/products')),
            ],
        ),
    ]