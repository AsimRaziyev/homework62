from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(ListView):
    model = Product
    template_name = "product/list_view.html"
    context_object_name = "products"
    ordering = "product_name"
    paginate_by = 6
    paginate_orphans = 1

    # def get_queryset(self):
    #     return super().get_queryset().filter(remainder__gt=0)


class DetailedView(DetailView):
    model = Product
    template_name = "product/detailed_view.html"


class CreateProduct(PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = "product/create_product.html"

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.add_product")


class UpdateProduct(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/update_product.html"

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.change_product")


class DeleteProduct(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "product/delete_product.html"
    success_url = reverse_lazy('webapp:index')

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.delete_product")
