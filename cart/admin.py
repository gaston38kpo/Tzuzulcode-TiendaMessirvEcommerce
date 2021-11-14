from django.contrib import admin
from .models import DiscountCode
from .models import Cart
from .models import CartProduct

# Register your models here.
admin.site.register(DiscountCode)
admin.site.register(Cart)
admin.site.register(CartProduct)
