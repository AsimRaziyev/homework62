from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    CATEGORY_CHOICES = [('Other', 'Разное'), ('IPad', 'IPad'), ('IPod', 'IPod'),
                        ('IPhone', 'IPhone'), ('AirPods', 'AirPods'),
                        ('MacOS', 'MacOS'), ('Apple Watch', 'Apple Watch')]
    product_name = models.CharField(max_length=100, blank=False, verbose_name="Product name")
    product_description = models.TextField(max_length=2000, blank=True, verbose_name="Product description")
    category = models.TextField(max_length=100, blank=False, verbose_name="Category",
                        default='Other', choices=CATEGORY_CHOICES)
    remainder = models.IntegerField(max_length=None, verbose_name="Remainder")
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Price")

    def get_absolute_url(self):
        return reverse("webapp:detailed_view", kwargs={"pk": self.pk})
