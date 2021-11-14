from django.shortcuts import render, redirect
from cart.models import Cart, CartProduct

# Create your views here.
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).get()
    cart_products = CartProduct.objects.filter(cart_fk=cart.id).all()

    return render(request, 'cart.html', context={'cart_products': cart_products})
        

def delete_product_from_cart(request, cart_product_id):
    cart_product = CartProduct.objects.filter(id= cart_product_id)
    cart_product.delete()

    return redirect('cart')

def sort_cart_products(request, sort):
    cart = Cart.objects.filter(user=request.user).get()
    cart_products = CartProduct.objects.filter(cart_fk=cart.id).all()

    if sort == 'quantity_asc':
        cart_products = cart_products.order_by('quantity')
    elif sort == 'quantity_desc':
        cart_products = cart_products.order_by('-quantity')
    elif sort == 'name_asc':
        cart_products = cart_products.order_by('product_fk__name')
    elif sort == 'name_desc':
        cart_products = cart_products.order_by('-product_fk__name')

    return render(request, 'cart.html', context={'cart_products': cart_products})