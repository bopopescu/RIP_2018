# Generated by Django 2.1.4 on 2019-01-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogIn', '0004_auto_20190105_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]