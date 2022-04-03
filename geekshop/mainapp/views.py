from django.shortcuts import render

# Create your views here.
from mainapp.models import Product, ProductCategories


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):

    content = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all()
    }

    return render(request, 'mainapp/products.html', content)
