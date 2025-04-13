from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200, default="title")
    image = models.CharField(max_length=200, default="image")
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0, null=True)


class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(null=True, default='')

