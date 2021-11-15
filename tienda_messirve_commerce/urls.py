"""tienda_messirve_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from usuarios.views import filter_page, home_view
from usuarios.views import login_view
from usuarios.views import logout_view
from usuarios.views import register_view
from cart.views import add_product_to_cart, add_remove_one_product
from cart.views import add_order, cart_view
from cart.views import delete_product_from_cart
from cart.views import sort_cart_products
from orders.views import order_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),
<<<<<<< HEAD
    path('filter_product/', filter_page, name='product'),
=======
    path('home/', home_view, name='home'),

>>>>>>> 04cd840a4f726447713c58a627e96c9bb11d3690
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:product_id>', add_product_to_cart, name='add_product_to_cart'),
    path('cart/del/<int:cart_product_id>/', delete_product_from_cart, name='delete_product_from_cart'),
    path('cart/sort/<str:sort>/', sort_cart_products, name='sort_cart_products'),
    path('cart/add_order', add_order, name='add_order'),
    path('cart/add_remove_one_product/<str:quantity_func>/<str:product_id>/', add_remove_one_product, name='add_remove_one_product'),


    path('orders/', order_view, name='orders')
] + static(settings.STATIC_URL)
