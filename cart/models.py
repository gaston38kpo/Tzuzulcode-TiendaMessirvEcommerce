from django.db import models

# Create your models here.

class Cart(models.Model):
    """ Model to represent shopping cart """
    cart_id = models.BigAutoField()
    username = models.OneToOneField("User")
    discount_code = models.ManyToOneRel("DiscountCode")
    products = models.ManyToManyRel()

class DiscountCode(models.Model):
    """ Model to represent discount codes """
    code = models.BigAutoField()
    discount = models.IntegerField()