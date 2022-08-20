from django import forms
from django.forms import widgets
from webapp.models import Product, ItemInCart, Order


class ProductForm(forms.ModelForm):
    remainder = forms.IntegerField(min_value=0)
    price = forms.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        model = Product
        fields = ["product_name", "product_description", "category", "remainder", "price"]
        widgets = {
            "product_description": widgets.Textarea(attrs={"placeholder": "введите текст", "cols": 30, "rows": 3})
        }


class ItemCartForm(forms.ModelForm):

    class Meta:
        model = ItemInCart
        fields = ["quantity"]


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["name", "phone", "address"]

