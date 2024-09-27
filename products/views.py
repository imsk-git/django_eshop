from django.shortcuts import get_object_or_404, redirect, render

from products.forms import ProductForm
from products.models import Product
from django.contrib import messages

# Create your views here.

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html',{'products':products})


def single_product(request,id):
    product = get_object_or_404(Product, id=id)
    data = {
        'product':product
    }
    return render(request, 'single_product.html', data)


def add_to_cart(request,id):
    return redirect('product')

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
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
        product_image = request.FILES.get('image')
        product_category = request.POST.get('category','')

        if product_image:
            Product.objects.create(
                title=product_title,
                description=product_description,
                price=product_price,
                image=product_image,
                category_id=product_category
            )

        # Product.objects.create(title=product_title,description=product_description,price=product_price,image=product_image,category_id=product_category)
            messages.success(request, 'Product added successfully.')
            return redirect('add_product')
    
        else:
            error_message = "Image is required."
            return render(request, 'add_product.html', {'error_message': error_message})
    
    
    return render(request, 'add_product.html')