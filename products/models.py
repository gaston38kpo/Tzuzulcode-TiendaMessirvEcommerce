from django.db import models

# Create your models here.

class Product(models.Model):
    """ Model to represent products """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=64)
    description = models.TextField(null=True)
    price = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(default=0)
    img_path = models.CharField(max_length=512)