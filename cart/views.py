from django.shortcuts import redirect, render
from .models import Cart
from .models import CartProduct
from products.models import Product
from orders.models import Order, OrderProduct
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


def add_remove_one_product(request, quantity_func, product_id):
    cart = Cart.objects.filter(user=request.user).get()
    cart_product = CartProduct.objects.filter(cart_fk=cart.id, product_fk = product_id)
    product = Product.objects.filter(id=product_id)

    quantity = cart_product.get().quantity
    if quantity_func == "add_product":
        if quantity < product.get().stock:
            cart_product.update(quantity=quantity+1)
    elif quantity_func == "remove_product":
        if quantity > 1:
            cart_product.update(quantity=quantity-1)
        
    return redirect('cart')
    