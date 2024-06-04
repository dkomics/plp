# labridge_app/urls.py

from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page URL
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),
]


