from django.shortcuts import redirect, render
from .models import Cart
from .models import CartProduct
from products.models import Product

# Errors 
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseServerError
from django.http import HttpResponseNotFound

# Create your views here.


def add_product_to_cart(request, product_id):
    redirect_url = request.META.get('HTTP_REFERER', 'home')
    error_template = "ERROR: {0}. <a href=\"/home/\">HOME</a>"

    # 405 Method Not Allowed
    if not request.method == "POST":        
        return HttpResponseNotAllowed(error_template.format("only POST method allowed"))

    # unautheticated user with cart
    if not request.user.is_authenticated:
        return HttpResponseBadRequest(error_template.format( "login required"))

    # Get cart
    cart = Cart.objects.filter(user=request.user)

    # 500 user doesn't have cart
    if not cart:
        return HttpResponseServerError(error_template.format("user doesn't have cart"))

    cart = cart[0]

    # Check if product is already in cart
    product = cart.products.filter(id=product_id)
    product_is_already_in_cart = True

    # If not, get from Product
    if not product:
        product_is_already_in_cart = False
        product = Product.objects.filter(id=product_id)

    # 404 Product not found
    if not product:
        return HttpResponseNotFound(error_template.format("product not found"))

    product = product[0]
    quantity_to_add = int(request.POST["quantity"])

    # 400 Bad Request (invalid quantity)
    if quantity_to_add <= 0:
        return HttpResponseBadRequest(error_template.format("invalid quantity, quantity must be a positive integer."))

    if product_is_already_in_cart:
        cart_product = CartProduct.objects.filter(cart_fk=cart, product_fk=product).get()
        total_quantity = cart_product.quantity + quantity_to_add
        # 400 Bad Request (invalid total quantity)
        if total_quantity > product.stock:
            return HttpResponseBadRequest(error_template.format("can't set more quantity than current stock."))
        cart_product.quantity = total_quantity
    else:
        cart_product = CartProduct(
            cart_fk=cart,
            product_fk=product,
            quantity=quantity_to_add
        )

    cart_product.save()

    return redirect(redirect_url)
