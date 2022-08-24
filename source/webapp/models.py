from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import Sum, F
from django.urls import reverse


class Product(models.Model):
    CATEGORY_CHOICES = [('Other', 'Разное'), ('IPad', 'IPad'), ('IPod', 'IPod'),
                        ('IPhone', 'IPhone'), ('AirPods', 'AirPods'),
                        ('MacOS', 'MacOS'), ('Apple Watch', 'Apple Watch')]
    product_name = models.CharField(max_length=100, blank=False, verbose_name="Product name")
    product_description = models.TextField(max_length=2000, blank=True, verbose_name="Product description")
    category = models.CharField(max_length=20, blank=False, verbose_name="Category",
                        default='Other', choices=CATEGORY_CHOICES)
    remainder = models.IntegerField(max_length=None, verbose_name="Remainder")
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Price")

    def __str__(self):
        return f'{self.product_name} - {self.remainder}'

    def get_absolute_url(self):
        return reverse("webapp:detailed_view", kwargs={"pk": self.pk})


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    phone = models.CharField(max_length=30, verbose_name="Phone")
    address = models.CharField(max_length=100, verbose_name="Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date creation")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, related_name="orders",
                                verbose_name='User')

    def __str__(self):
        return f'{self.name} - {self.phone}'

    def get_total(self):
        total = self.order_products.aggregate(total=Sum(F("quantity") * F("product__price")))
        return total["total"]



class OrderProduct(models.Model):
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE,
                                verbose_name="Product", related_name="products_order")
    order = models.ForeignKey("webapp.Order", on_delete=models.CASCADE,
                              verbose_name="Order", related_name="order_products")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")

    def __str__(self):
        return f'{self.product.product_name} - {self.order.name}'

    def get_sum(self):
        return self.quantity * self.product.price
