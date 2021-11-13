from django.db import models

# Create your models here.

class Product(models.Model):
    """ Model to represent products """
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, max_length=1024)
    stock = models.PositiveIntegerField(default=0)
    img_path = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"id:{self.id} ({self.stock}) {self.name} ${self.price}"
        
        
