from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=255)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
        