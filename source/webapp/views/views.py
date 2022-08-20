from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(ListView):
    model = Product
    template_name = "product/list_view.html"
    context_object_name = "products"
    ordering = "product_name"
    paginate_by = 4
    paginate_orphans = 1

    # def get_queryset(self):
    #     return super().get_queryset().filter(remainder__gt=0)


class DetailedView(DetailView):
    model = Product
    template_name = "product/detailed_view.html"


class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = "product/create_product.html"


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/update_product.html"


class DeleteProduct(DeleteView):
    model = Product
    template_name = "product/delete_product.html"
    success_url = reverse_lazy('webapp:index')
