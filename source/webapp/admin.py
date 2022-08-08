from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_description', 'category', 'remainder', 'price']


admin.site.register(Product, ProductAdmin)
