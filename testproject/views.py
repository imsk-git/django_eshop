
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render

from categories.models import Category
from products.models import Banner, Product

# def index(request):
#     return render(request, 'index.html')

def home(request):
    banners = Banner.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    data = {
        'banners':banners,
        'categories':categories,
        'products':products
    }
    return render(request, 'home.html', data)

# or do this for title 
# def home(request):
#     data = {'title': "Eshop | HomePage"}
#     return render(request, 'home.html', data)


def about(request):
    return render(request, 'about.html')



