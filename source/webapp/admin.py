from django.contrib import admin

# Register your models here.
from webapp.models import Product, OrderProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_description', 'category', 'remainder', 'price']

admin.site.register(Product, ProductAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'order', 'quantity']

admin.site.register(OrderProduct, OrderProductAdmin)

