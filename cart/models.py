from django.db import models
from products.models import Product
from usuarios.models import Customer

class Cart_item(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.cart_item_id)