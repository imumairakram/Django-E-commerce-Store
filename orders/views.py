from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import Order
from products.models import Product
from .models import Order, OrderItem



@login_required
def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.warning(request, "Your cart is empty!")
        return redirect("view_cart")

    order = Order.objects.create(user=request.user, total_price=0)
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total_price += subtotal

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price,
        )

    order.total_price = total_price
    order.save()

    # clear cart
    request.session["cart"] = {}

    messages.success(request, f"Order #{order.id} placed successfully!")
    return redirect("order_success", order_id=order.id)


@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, "orders/success.html", {"order": order})

@login_required
def checkout(request):
    if request.method == "POST":
        # temporary: just create empty order
        order = Order.objects.create(user=request.user, status="pending")
        return redirect("order_success", order_id=order.id)

    return render(request, "orders/checkout.html")

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/my_orders.html", {"orders": orders})