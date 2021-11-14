from django.shortcuts import redirect, render
from .models import Cart
from .models import CartProduct
from products.models import Product

# Create your views here.


def add_product_to_cart(request, product_id):
    redirect_url = request.META.get('HTTP_REFERER', 'home')

    # TODO: 405 Method Not Allowed
    if not request.method == "POST":
        return redirect(redirect_url)

    # TODO: unautheticated user with cart
    if not request.user.is_authenticated:
        return redirect(redirect_url)

    # Get cart
    cart = Cart.objects.filter(user=request.user)

    # TODO: 500 user doesn't have cart
    if not cart:
        return redirect(redirect_url)

    cart = cart[0]
    
    product = Product.objects.filter(id=product_id)

    # TODO: 404 Product not found
    if not product:
        return redirect(redirect_url)

    product = product[0]
    quantity_to_add = int(request.POST["quantity"])

    # TODO: 400 Bad Request (invalid quantity)
    if quantity_to_add <= 0:
        return redirect(redirect_url)

    cart_product = CartProduct(
        cart_fk=cart,
        product_fk=product,
        quantity=request.POST["quantity"]
    )

    cart_product.save()

    return redirect(redirect_url)
