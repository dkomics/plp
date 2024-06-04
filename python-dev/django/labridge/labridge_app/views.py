# views.py
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Category, Product, Order, OrderItem

def landing_page(request):
    """
    Render the landing page.
    """
    return render(request, 'labridge_app/landing_page.html')

def product_list(request):
    """
    Render the product list page with all categories and products.
    """
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'labridge_app/product_list.html', {'categories': categories, 'products': products})

def product_detail(request, product_id):
    """
    Render the product detail page for the given product ID.
    """
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'labridge_app/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    """
    Add a product to the user's cart. If the product is already in the cart,
    increment the quantity by one.
    """
    product = get_object_or_404(Product, pk=product_id)
    order, created = Order.objects.get_or_create(user=request.user, completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if created:
        order_item.quantity = 1
    else:
        order_item.quantity += 1
    order_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    """
    Render the cart detail page for the current user's active order.
    """
    order = get_object_or_404(Order, user=request.user, completed=False)
    return render(request, 'labridge_app/cart_detail.html', {'order': order})

@login_required
def checkout(request):
    """
    Handle the checkout process. If the request method is POST, complete the order
    and redirect to the order history page.
    """
    order = get_object_or_404(Order, user=request.user, completed=False)
    if request.method == 'POST':
        order.completed = True
        order.save()
        return redirect('order_history')
    return render(request, 'labridge_app/checkout.html', {'order': order})

@login_required
def order_history(request):
    """
    Render the order history page with all completed orders for the current user.
    """
    orders = Order.objects.filter(user=request.user, completed=True)
    return render(request, 'labridge_app/order_history.html', {'orders': orders})
