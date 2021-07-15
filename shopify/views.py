from django.shortcuts import render
from .models import Product


def getProducts(request):
    context = {
        "Products": Product.objects.all()
    }

    return render(request, "product_list.html", context)
