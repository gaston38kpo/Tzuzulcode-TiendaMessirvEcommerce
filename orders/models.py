from django.db import models
from django.contrib.auth.models import User
from cart.models import DiscountCode
from products.models import Product

class Order(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)    
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.BooleanField(default=False)    
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, through='OrderProduct')


    def __str__(self):
        return f"{self.id} {self.order_fk.user_fk.username} ${self.order_fk.total}"

class OrderProduct(models.Model):
    order_fk = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_fk = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id} {self.order_fk.user_fk.username} ${self.price * self.quantity}"
        