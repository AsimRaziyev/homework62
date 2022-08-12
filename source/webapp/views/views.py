from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(ListView):
    model = Product
    template_name = "list_view.html"
    context_object_name = "products"
    ordering = "product_name"
    paginate_by = 4
    paginate_orphans = 1


class DetailedView(DetailView):
    template_name = "detailed_view.html"
    model = Product


class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = "create_product.html"


class UpdateProduct(UpdateView):
    form_class = ProductForm
    template_name = "update_product.html"
    model = Product


class DeleteProduct(DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = reverse_lazy('webapp:index')
