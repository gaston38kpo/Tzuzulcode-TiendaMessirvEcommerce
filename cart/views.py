from django.shortcuts import redirect, render
from .models import Cart
from .models import CartProduct
from products.models import Product

# Create your views here.

def add_product_to_cart(request, product_id):
    redirect_url = request.META.get('HTTP_REFERER', '/home/')
    if not request.method == "POST":
        return redirect(redirect_url)

    if not  request.user.is_authenticated:
        return redirect(redirect_url)

    cart = Cart.objects.filter(user=request.user)

    if not cart:
        return redirect(redirect_url)

    cart = cart[0]
    
    product = Product.objects.filter(id=product_id)

    if not product:
        return redirect(redirect_url)

    product = product[0]

    cart_product = CartProduct(
        cart_fk=cart,
        product_fk=product,
        quantity=request.POST["quantity"]
    )

    cart_product.save()

    return redirect(redirect_url)
