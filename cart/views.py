from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

# ✅ View Cart
def view_cart(request):
    cart = request.session.get("cart", {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        subtotal = product.price * quantity
        total += subtotal
        products.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal
        })

    return render(request, "cart/cart.html", {"products": products, "total": total})


# ✅ Add to Cart
def add_to_cart(request, pk):
    cart = request.session.get("cart", {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session["cart"] = cart
    return redirect("view_cart")


# Update cart quantity
def update_cart(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart = request.session.get("cart", {})
        if str(product_id) in cart:
            cart[str(product_id)] = quantity
        request.session["cart"] = cart
    return redirect("view_cart")


# Remove item from cart
def remove_from_cart(request, product_id):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        if str(product_id) in cart:
            del cart[str(product_id)]
        request.session["cart"] = cart
    return redirect("view_cart")
