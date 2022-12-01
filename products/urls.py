from django.urls import path
from products.views import products_view, detail_product_view, categories_view, product_create_view


urlpatterns = [
    path('products/', products_view),
    path('products/<int:id>/', detail_product_view),
    path('category/', categories_view),
    path('products/create/', product_create_view)
]

