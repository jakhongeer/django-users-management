from django.shortcuts import render
from .models import Product


def getProducts(request):
    context = {
        "Products": Product.objects.all()
    }

    return render(request, "product_list.html", context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
