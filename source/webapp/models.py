from django.db import models

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [('Other', 'Разное'), ('IPad', 'IPad'), ('IPod', 'IPod'),
                        ('IPhone', 'IPhone'), ('AirPods', 'AirPods'),
                        ('MacOS', 'MacOS'), ('Apple Watch', 'Apple Watch')]
    product_name = models.CharField(max_length=100, blank=True, verbose_name="Наименование товара")
    product_description = models.TextField(max_length=2000, blank=False, verbose_name="Описание товара")
    category = models.TextField(max_length=100, blank=True, verbose_name="Категория",
                        default='Other', choices=CATEGORY_CHOICES)
    remainder = models.IntegerField(max_length=None, verbose_name="Остаток")
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Стоимость")
