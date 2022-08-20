from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from webapp.models import ItemInCart, Product, Order, OrderProduct
from webapp.forms import ItemCartForm, OrderForm


class ItemCartAdd(CreateView):
    model = ItemInCart
    form_class = ItemCartForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        quantity = form.cleaned_data.get("quantity")
        if quantity > product.remainder:
            pass
        else:
            try:
                item_cart_product = ItemInCart.objects.get(product=product)
                item_cart_product.quantity += quantity
                item_cart_product.save()
            except ItemInCart.DoesNotExist:
                ItemInCart.objects.create(product=product, quantity=quantity)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("webapp:index")


class ItemCartView(ListView):
    model = ItemInCart
    template_name = "item_cart/item_cart_view.html"
    context_object_name = "item_cart"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['total'] = ItemInCart.get_total()
        context['form'] = OrderForm()
        return context


class ItemCartDelete(DeleteView):
    model = ItemInCart
    success_url = reverse_lazy('webapp:item_cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ItemCartDeleteOne(DeleteView):
    model = ItemInCart
    success_url = reverse_lazy('webapp:item_cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        item_cart = self.object
        item_cart.quantity -= 1
        if item_cart.quantity < 1:
            item_cart.delete()
        else:
            item_cart.save()
        return HttpResponseRedirect(success_url)


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('webapp:index')

    # def form_valid(self, form):
    #     order = form.save()
    #     for item in ItemInCart.objects.all():
    #         OrderProduct.objects.create(product=item.product, quantity=item.quantity, order=order)
    #         item.product.remainder -= item.quantity
    #         item.product.save()
    #         item.delete()
    #
    #     return HttpResponseRedirect(self.success_url)

    def form_valid(self, form):
        order = form.save()

        products = []
        order_products = []

        for item in ItemInCart.objects.all():
            order_products.append(OrderProduct(product=item.product, quantity=item.quantity, order=order))
            item.product.remainder -= item.quantity
            products.append(item.product)

            OrderProduct.objects.bulk_create(order_products)
            Product.objects.bulk_update(products, ("remainder",))
            ItemInCart.objects.all().delete()

        return HttpResponseRedirect(self.success_url)
