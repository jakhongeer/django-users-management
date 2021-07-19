from django.contrib import admin
from .models import Category, Product, Order, OrderedItem
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderedItem)
class OrderedItemAdmin(admin.ModelAdmin):
    pass
