from django.shortcuts import render

from products.models import Product

# Create your views here.

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html',{'products':products})


def single_product(request,id):
    single_products = Product.objects.get(id=id)
    data = {
        'products':single_products
    }
    return render(request, 'single_product.html', data)


def add_to_cart(request,id):
    return render(request, 'add_to_cart')