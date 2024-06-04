# labridge_app/admin.py
from django.contrib import admin # type: ignore
from .models import Supplier, Category, Product, Order, OrderItem

admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

