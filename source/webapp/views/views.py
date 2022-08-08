from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from webapp.models import Product


class IndexView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"