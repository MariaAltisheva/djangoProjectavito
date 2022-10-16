from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=2000, null=True)
    address = models.CharField(max_length=500)
    is_published = models.BooleanField()