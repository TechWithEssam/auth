from django.shortcuts import render, redirect
from .models import Cart, Order
# Create your views here.


def cart_customer_view(request) :
    user, _ = Order.objects.new_or_get(request)
    obj = user.cart_set.all()
    if request.user.is_authenticated :
        obj = Cart.objects.filter(order__user=request.user)
    context = {
        "obj":obj
    }
    return render(request, "items/cart.html", context)


def add_to_cart_view(request) :
    if request.method == "POST" :
        product_id = request.POST.get("product_id")
        color = request.POST.get("color")
        print(color)
        print(product_id)
        return redirect(request.META.get('HTTP_REFERER'))