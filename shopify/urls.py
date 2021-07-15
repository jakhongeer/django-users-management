from django.urls import path
from . import views

app_name = "shopify"

urlpatterns = [
    path('products/', views.getProducts, name="products")
]
