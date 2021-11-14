from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class DiscountCode(models.Model):
    """ Model to represent discount codes """
    code = models.CharField(primary_key=True, max_length=32)
    discount = models.PositiveIntegerField()

    def __str__(self):        
        return f"code: {self.code} discount: {self.discount}"

class Cart(models.Model):
    """ Model to represent shopping cart """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, through='CartProduct')
    
    def __str__(self):
       return f"id:{self.id} username: {self.user.username}"


class CartProduct(models.Model):
    cart_fk = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product_fk = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"id: {self.id} price: ${self.product_fk.price} quantity: ({self.quantity})"
    
    def subtotal(self):
        return self.quantity * self.product_fk.price
