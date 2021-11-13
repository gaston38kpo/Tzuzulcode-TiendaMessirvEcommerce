from django.contrib import admin
from .models import DiscountCode, Cart, CartProduct

# Register your models here.
admin.site.register(DiscountCode)
admin.site.register(Cart)
admin.site.register(CartProduct)