# views.py
from http.client import HTTPResponse
from tkinter import Canvas
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.core.mail import send_mail # type: ignore
from django.template.loader import render_to_string # type: ignore
from django.utils.html import strip_tags # type: ignore
from django.conf import settings # type: ignore

from django.shortcuts import render, get_object_or_404 # type: ignore
from django.core.files.storage import FileSystemStorage # type: ignore
from io import BytesIO
from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.pdfgen import canvas # type: ignore

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
    product = get_object_or_404(Product, pk=product_id)
    order, created = Order.objects.get_or_create(user=request.user, completed=False)
    
    # Retrieve the quantity from the form data
    quantity = int(request.POST.get('quantity', 1))
    
    # Check if there is enough stock available
    if product.stock >= quantity:
        # Check if the product is already in the cart
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        
        # If the order item already exists, update the quantity
        if not created:
            order_item.quantity += quantity
        else:
            order_item.quantity = quantity
        order_item.save()
        
        # Update the product's stock
        product.stock -= quantity
        product.save()
    else:
        # Handle insufficient stock error
        # You can redirect the user to the product page with an error message
        pass
    
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
        # Send order information to vendor's email
        # subject = f'New Order: #{order.id}'
        # html_message = render_to_string('labridge_app/vendor_order_email.html', {'order': order}) # type: ignore
        # plain_message = strip_tags(html_message) # type: ignore
        # from_email = settings.DEFAULT_FROM_EMAIL
        # to_email = 'pipettewise@gmail.com'  # Replace with vendor's email address
        # send_mail(subject, plain_message, from_email, [to_email], html_message=html_message) # type: ignore

        order.completed = True
        order.save()
        return redirect('order_history')
    return render(request, 'labridge_app/checkout.html', {'order': order})

def order_detail(request, order_id):
    """
    Render the detailed view of a specific order.
    """
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'labridge_app/order_detail.html', {'order': order})

@login_required
def order_history(request):
    """
    Render the order history page with all completed orders for the current user.
    """
    orders = Order.objects.filter(user=request.user, completed=True)
    return render(request, 'labridge_app/order_history.html', {'orders': orders})

def generate_order_summary_pdf(order):
    # Create a PDF buffer
    buffer = BytesIO()

    # Create a PDF document
    pdf = Canvas.Canvas(buffer, pagesize=A4) # type: ignore
    pdf.drawString(100, 750, f'Order Summary: #{order.id}')
    # Add order details to the PDF
    # Example: pdf.drawString(100, 700, f'Customer: {order.customer}')
    # Add more order details as needed

    # Save the PDF document
    pdf.save()

    # Set the buffer's file pointer to the beginning
    buffer.seek(0)

    return buffer

def download_order_summary(request, order_id):
    # Retrieve order details from the database
    order = get_object_or_404(Order, pk=order_id)

    # Generate order summary PDF
    buffer = generate_order_summary_pdf(order)

    # Create HTTP response
    response = HTTPResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_summary_{order.id}.pdf"'

    return response