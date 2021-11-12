from django.db import models

# Create your models here.

class Product(models.Model):
    """ Model to represent products """
    product_id = models.BigAutoField()
    name = models.CharField(null=False)
    description = models.TextField(null=True)
    price = models.FloatField(default=0.0, min=0.0)
    stock = models.IntegerField(default=0, min=0)
    img_path = models.ImageField()  # Use CharField to store img_path?