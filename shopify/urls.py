from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.getProducts, name="products"),
    path('store/', views.store, name="store",),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
