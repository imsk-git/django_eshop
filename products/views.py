from django.shortcuts import redirect, render

from products.forms import ProductForm
from products.models import Product

# Create your views here.

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html',{'products':products})


def single_product(request,id):
    single_products = Product.objects.get(id=id).first()
    data = {
        'products':single_products
    }
    return render(request, 'single_product.html', data)


def add_to_cart(request,id):
    return redirect('product')


# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('product')
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html',{'form':form})

def add_product(request):
    if request.method == 'POST':
        product_title = request.POST.get('title','')
        product_description = request.POST.get('description','')
        product_price = request.POST.get('price','')
        product_image = request.POST.get('image','')
        product_category = request.POST.get('category','')

        Product.objects.create(title=product_title,description=product_description,price=product_price,image=product_image,category_id=product_category)

        return redirect('add_product')
    return render(request, 'add_product.html')