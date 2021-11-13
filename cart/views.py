from django.shortcuts import render, redirect
from cart.models import Cart
from products.models import Product

# Create your views here.
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).get()
    return render(request, 'cart.html', context={'cart': cart.products.all()})
        

def delete_product_to_cart(request, product_id):
    prod = Product.objects.filter(id=product_id).get()
    cart = Cart.objects.filter(user=request.user).get()
    cart.products.remove(prod)

    return redirect('cart')

def order_products_by_price(request):
    cart = Cart.objects.filter(user=request.user).get()
    cart.products.order_by('price')
    return redirect('cart')