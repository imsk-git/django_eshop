from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required

from categories.forms import CategoryForm
from categories.models import Category
from products.forms import ProductForm
from products.models import Product

# Create your views here.

@login_required(login_url='admin_login')
def admin_dashboard(request):
    return render(request, 'admin_panel/index.html')

@login_required(login_url='admin_login')
def products(request):
    product_list = Product.objects.all()  # Fetch all products
    categories = Category.objects.all()   # Fetch all categories
    return render(request, 'admin_panel/products.html', {
        'products': product_list,
        'categories': categories
    })

def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('admin_add_product')
        else:
            messages.error(request, 'Please correct the errors below.')
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, 'admin_panel/add-product.html',{'form':form, 'categories':categories})
    # if request.method == 'POST':
    #     messages.success(request, 'Product added successfully.')
    #     return redirect('admin_add_product')
    # return render(request, 'admin_panel/add-product.html')

def edit_product(request, id):
    return render(request, 'admin_panel/edit-product.html', {'id': id})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('admin_add_category')
        else:
            messages.error(request, 'Please correct the errors below.')
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'admin_panel/add-category.html',{'form':form})

# def category_detail(request, id):
#     # Get the category based on the category_id
#     category = get_object_or_404(Category, id=id)
    
#     products = category.products.all()

#     # Render a template and pass the category to the context
#     return render(request, 'single_category.html', {'category': category, 'products': products})

@login_required(login_url='admin_login')
def accounts(request):
    return render(request, 'admin_panel/accounts.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # print(f"User logged in: {user.username}")
            return redirect('admin_dashboard')
        else:
            # print("Invalid credentials")
            messages.error(request, 'Invalid credentials.')
    return render(request, 'admin_panel/login.html', {'request': request})

def logout(request):
    auth_logout(request)
    return redirect('admin_login')

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect('admin_products')

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, 'Category deleted successfully.')
    return redirect('admin_products')