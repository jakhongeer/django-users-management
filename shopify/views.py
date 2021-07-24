from django.shortcuts import render
from .models import *


def getProducts(request):
    context = {
        "Products": Product.objects.all()
    }

    return render(request, "product_list.html", context)

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False) #see the documentation https://docs.djangoproject.com/en/3.2/ref/models/querysets/#get-or-create
        products = order.orderedproduct_set.all()
    else:
        products = []
        order = {'get_cart_total':0, 'get_cart_products':0}
    context = {'products': products, 'order': order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False) #see the documentation https://docs.djangoproject.com/en/3.2/ref/models/querysets/#get-or-create
        products = order.orderedproduct_set.all()
    else:
        products = []
        order = {'get_cart_total':0, 'get_cart_products':0}
    context = {'products': products, 'order': order}
    return render(request, 'store/checkout.html', context)
