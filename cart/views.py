from django.shortcuts import render, redirect
from cart.models import Cart, CartProduct
from orders.models import Order, OrderProduct
# Create your views here.
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).get()
    cart_products = CartProduct.objects.filter(cart_fk=cart.id).all()
    
    # En caso no hayan productos se redirecciona al home(cambiar por url productos)
    if(len(cart_products)==0):
        return redirect('home')
    
    first = cart_products[0]
    return render(request, 'cart.html', context={'cart_products': cart_products,
                                                 'first': first})
        
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

    first = cart_products.all()[0]
    return render(request, 'cart.html', context={'cart_products': cart_products,
                                                    'first': first})

def add_order(request):
    cart = Cart.objects.filter(user=request.user)
    if(len(cart) == 0):
        return redirect('cart')
    
    cart = cart.get()
    
    cart_products = CartProduct.objects.filter(cart_fk=cart.id).all()
    if(len(cart_products)==0):
        return redirect('cart')
    
    cart_products = cart_products.all()

    new_order = Order(
        user_fk = cart.user,    
        total = CartProduct.total,
        discount_code = cart.discount_code,
    ) 
    new_order.save()
    
    for cart_product in cart_products:
        order_product = OrderProduct(
            order_fk = new_order,
            product_fk = cart_product.product_fk,
            price = cart_product.product_fk.price,
            quantity = cart_product.quantity,
        ) 
        order_product.save()
        cart_product.delete()
       
    #TODO:Incluir lógica para descontar del inventario
    
    return redirect('orders')