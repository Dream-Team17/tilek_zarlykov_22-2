from django.shortcuts import render
from products.models import Product, Category

# Create your views here.

def products_view(request):
    if request.method == "GET":
        products = [{
            "id": product.id,
            "title": product.title,
            "image": product.image,
            "description": product.description,
            "price": product.price,
            "category": product.category
        } for product in Product.objects.all() ]

        data = {
            'products':products
        }

        return render(request, "products/products.html", context=data)

