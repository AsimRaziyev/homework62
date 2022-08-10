from django.urls import path

from webapp.views.views import IndexView, DetailedView, CreateProduct, UpdateProduct, DeleteProduct

app_name = "webapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<int:pk>/", DetailedView.as_view(), name="detailed_view"),
    path("product/new/", CreateProduct.as_view(), name="create_product"),
    path("product/<int:pk>/update/", UpdateProduct.as_view(), name="update_product"),
    path("product/<int:pk>/delete/", DeleteProduct.as_view(), name="delete_product"),
]
