from django.shortcuts import render

# Create your views here.
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Product, Order, OrderItem



def home(request):
    if Product.objects.count() == 0:
        Product.objects.create(name="Laptop", price_cents=50000)
        Product.objects.create(name="Headphones", price_cents=15000)
        Product.objects.create(name="Mouse", price_cents=3000)
        
    products = Product.objects.all().order_by("id")
    orders = Order.objects.filter(status="paid").order_by("-created_at")

    return render(
        request,
        "shop/home.html",
        {
            "products": products,
            "orders": orders,
        },
    )


@require_POST
def create_checkout_session(request):
    products = Product.objects.all()

    order = Order.objects.create(status="pending", total_cents=0)
    total_cents = 0

    for product in products:
        qty_str = request.POST.get(f"qty_{product.id}", "0")
        try:
            qty = int(qty_str)
        except ValueError:
            qty = 0

        if qty <= 0:
            continue

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=qty,
            price_cents=product.price_cents,
        )

        total_cents += product.price_cents * qty

    if total_cents == 0:
        order.delete()
        return redirect("/")

    order.total_cents = total_cents
    order.save()

    return redirect(f"/mock-checkout/{order.id}/")


def success(request):
    # Optional: show success page
    return render(request, "shop/success.html")


def cancel(request):
    return render(request, "shop/cancel.html")

def mock_checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.status == "paid":
        return redirect("/")

    return render(request, "shop/mock_checkout.html", {"order": order})


@require_POST
def mock_pay(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Prevent double payment
    if order.status != "paid":
        order.status = "paid"
        order.save()

    return redirect("/")


@require_POST
def mock_cancel(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.status == "pending":
        order.status = "canceled"
        order.save()

    return redirect("/")