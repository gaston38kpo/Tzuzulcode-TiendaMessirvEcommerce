from django.shortcuts import redirect, render
from .models import Cart
from .models import CartProduct
from products.models import Product

# Create your views here.

def add_product_to_cart(request, product_id):
    if not request.method == "POST":
        return redirect(request.META.get('HTTP_REFERER'))

    if not  request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER'))

    cart = Cart.objects.filter(user=request.user)

    if not cart:
        return redirect(request.META.get('HTTP_REFERER'))

    cart = cart[0]
    
    product = Product.objects.filter(id=product_id)

    if not product:
        return redirect(request.META.get('HTTP_REFERER'))

    product = product[0]

    cart_product = CartProduct(
        cart_fk=cart,
        product_fk=product,
        quantity=request.POST["quantity"]
    )

    cart_product.save()

    return redirect(request.META.get('HTTP_REFERER'))
