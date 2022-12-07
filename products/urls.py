from django.urls import path
from products.views import (
    DetailProductView,
    ProductsCreateView,
    CategoryView,
    ProductsView
    )


urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/<int:id>/', DetailProductView.as_view()),
    path('category/', CategoryView.as_view()),
    path('products/create/', ProductsCreateView.as_view())
]

