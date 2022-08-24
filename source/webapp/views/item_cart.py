from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from webapp.models import Product, Order, OrderProduct
from webapp.forms import OrderForm


class ItemCartAdd(View):

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        quantity = int(self.request.POST.get("quantity"))
        if quantity > product.remainder:
            return HttpResponseBadRequest(
                f"Количество товара {product.product_name} всего {product.remainder}. Добавить {quantity} штук не получится"
            )
        else:
            cart = self.request.session.get("cart", {})
            if str(product.pk) in cart:
                cart[str(product.pk)] += quantity
            else:
                cart[str(product.pk)] = quantity
            self.request.session["cart"] = cart
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("webapp:index")


class ItemCartView(TemplateView):
    template_name = "item_cart/item_cart_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get("cart", {})
        products = []
        total = 0
        for pk, quantity in cart.items():
            product = Product.objects.get(pk=pk)
            product_total = quantity * product.price
            total += product_total
            products.append({"product": product, "quantity": quantity, "product_total": product_total})
        context['cart'] = products
        context['total'] = total
        context['form'] = OrderForm()
        return context


class ItemCartDelete(View):

    def get(self, request, pk, *args, **kwargs):
        cart = self.request.session.get("cart", {})
        if str(pk) in cart:
            cart.pop(str(pk))
            self.request.session["cart"] = cart
        return redirect("webapp:item_cart")


class ItemCartDeleteOne(View):

    def get(self, request, pk, *args, **kwargs):
        cart = self.request.session.get("cart", {})
        if str(pk) in cart:
            cart[str(pk)] -= 1
            if cart[str(pk)] < 1:
                cart.pop(str(pk))
            self.request.session["cart"] = cart
        return redirect("webapp:item_cart")


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        order = form.save(commit=False)
        if self.request.user.is_authenticated:
            order.user = self.request.user
        order.save()

        products = []
        order_products = []
        cart = self.request.session.get("cart", {})
        if cart:
            for pk, quantity in cart.items():
                product = Product.objects.get(pk=pk)
                order_products.append(OrderProduct(product=product, quantity=quantity, order=order))
                product.remainder -= quantity
                products.append(product)

            OrderProduct.objects.bulk_create(order_products)
            Product.objects.bulk_update(products, ("remainder",))
            self.request.session.pop('cart')

        return HttpResponseRedirect(self.success_url)
