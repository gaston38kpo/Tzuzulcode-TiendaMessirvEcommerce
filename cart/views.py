from django.shortcuts import render, redirect
from cart.models import Cart

# Create your views here.
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)[0]
    return render(request, 'cart.html', context={'cart': cart})
        

def delete_cart_item(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

