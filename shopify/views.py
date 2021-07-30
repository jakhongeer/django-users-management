from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


def getProducts(request):
    context = {
        "Products": Product.objects.all()
    }

    return render(request, "product_list.html", context)

def store(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False) #see the documentation https://docs.djangoproject.com/en/3.2/ref/models/querysets/#get-or-create
        products = order.orderedproduct_set.all()
    else:
        products = []
        order = {'get_cart_total':0, 'get_cart_products':0, 'shipping': False}
    products = Product.objects.all()
    context = {'products': products, 'shipping': False}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False) #see the documentation https://docs.djangoproject.com/en/3.2/ref/models/querysets/#get-or-create
        products = order.orderedproduct_set.all()
    else:
        products = []
        order = {'get_cart_total':0, 'get_cart_products':0, 'shipping': False}
    context = {'products': products, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False) #see the documentation https://docs.djangoproject.com/en/3.2/ref/models/querysets/#get-or-create
        products = order.orderedproduct_set.all()
    else:
        products = []
        order = {'get_cart_total':0, 'get_cart_products':0, 'shipping': False}
    context = {'products': products, 'order': order}
    return render(request, 'store/checkout.html', context)

def updateProduct(request):
    data = json.loads(request.body)
    print(data)
    
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, ordered=False)
    orderedProduct, created = OrderedProduct.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderedProduct.quantity = (orderedProduct.quantity + 1)
    elif action == 'remove':
        orderedProduct.quantity = (orderedProduct.quantity - 1)

    orderedProduct.save()

    if orderedProduct.quantity <=0:
        orderedProduct.delete()
    return JsonResponse('Product was added', safe=False)

@csrf_exempt
def processOrder(request):
    print('Data: ', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)
        #total = float(data['form']['total'])
        order.transaction_id = transaction_id
    #It should uncomment when the get_cart_total is fixed
        #if total == order.get_cart_total:
        #    order.ordered = True
        #order.save()
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer, 
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                region=data['shipping']['region'],
                country=data['shipping']['country']
            
            )
    return JsonResponse('Payment complete!', safe=False)

