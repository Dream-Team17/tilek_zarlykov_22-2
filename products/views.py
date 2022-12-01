from django.shortcuts import render, redirect
from products.models import Product, Category, Comment
from products.forms import ProductCreateForm, CommentCreateForm

# Create your views here.

def products_view(request):
    if request.method == "GET":
        category_id = request.GET.get('category_id')

        if category_id:
            products = Product.objects.filter(category__in=[category_id])
        else:
            products = Product.objects.all()

        products = [{
            "id": product.id,
            "title": product.title,
            "image": product.image,
            "description": product.description,
            "price": product.price,
            "category": product.category
        } for product in products]



        data = {
            'products':products
        }

        return render(request, "products/products.html", context=data)

def detail_product_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        comments = Comment.objects.filter(product_id=id)

        data = {
            'product': product,
            'comments': comments,
            'category': product.category,
            'form': CommentCreateForm
        }

        return render(request, 'products/detail.html', context=data)

    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                product_id=id
            )
            return redirect(f'/products/{id}/')
        else:
            product = Product.objects.get(id=id)
            comments = Comment.objects.filter(product_id=id)

            data = {
                'product': product,
                'comments': comments,
                'category': product.category,
                'form': form
            }

            return render(request, 'products/detail.html', context=data)


def categories_view(request, **kwargs):
    if request.method =='GET':
        categories = Category.objects.all()
        data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=data)

def product_create_view(request):
    if request.method == 'GET':
        data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=data)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),

            )


            return redirect('/products')
        else:
            data = {
                'form': form
            }
            return render(request, 'products/create.html', context=data)
