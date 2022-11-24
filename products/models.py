from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
