from django.shortcuts import render, redirect
from cart.models import Cart_item

# Create your views here.
def cart_view(request):
    cart = Cart_item.objects.all()    
    return render(request, 'cart.html', {'cart': cart})
        

def delete_cart_item(request, cart_item_id):
    cart_item = Cart_item.objects.get(cart_item_id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

