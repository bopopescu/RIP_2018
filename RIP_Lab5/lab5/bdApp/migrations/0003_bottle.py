# Generated by Django 2.1.5 on 2019-01-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bdApp', '0002_delete_bottle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
