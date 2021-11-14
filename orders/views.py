from django.shortcuts import render
from orders.models import Order, OrderProduct
from products.models import Product
# Create your views here.

def order_view(request):
    orders_with_products = []
    orders = Order.objects.all()
    for order in orders:
        order_products = OrderProduct.objects.filter(order_fk=order.id).all()
        products= []
        for order_product in order_products:
            product = Product.objects.filter(id=order_product.product_fk.id).get()
            products.append(product)
        orders_with_products.append((order, products))
        
    return render(request, 'order.html', context={'orders': orders_with_products})