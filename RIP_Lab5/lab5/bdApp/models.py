from django.db import models


class Bottle(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50)
    liter = models.IntegerField()


# Create your models here.
