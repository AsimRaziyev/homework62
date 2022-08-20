from django.urls import path

from webapp.views import IndexView, DetailedView, CreateProduct,\
    UpdateProduct, DeleteProduct, ItemCartAdd, ItemCartView, ItemCartDelete, ItemCartDeleteOne, OrderCreate


app_name = "webapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<int:pk>/", DetailedView.as_view(), name="detailed_view"),
    path("product/new/", CreateProduct.as_view(), name="create_product"),
    path("product/<int:pk>/update/", UpdateProduct.as_view(), name="update_product"),
    path("product/<int:pk>/delete/", DeleteProduct.as_view(), name="delete_product"),
    path("product/<int:pk>/add_item_cart/", ItemCartAdd.as_view(), name="add_item_cart"),
    path("item_cart/", ItemCartView.as_view(), name="item_cart"),
    path("item_cart/<int:pk>/delete/", ItemCartDelete.as_view(), name="delete_item_cart"),
    path("item_cart/<int:pk>/one_delete/", ItemCartDeleteOne.as_view(), name="delete_one_item_cart"),
    path("order/create/", OrderCreate.as_view(), name="order_create"),


]
