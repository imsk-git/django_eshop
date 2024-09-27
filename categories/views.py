from django.shortcuts import render, get_object_or_404
from .models import Category  # Assuming you have a Category model


def category(request):
    categories = Category.objects.all()
    return render(request,'category.html',{'categories':categories})

# def single_category(request,id):
#     category = Category.objects.get(id=id)
#     data = {
#         'category':category
#     }
#     return render(request, 'single_category.html', data)

def category_detail(request, id):
    # Get the category based on the category_id
    category = get_object_or_404(Category, id=id)
    
    products = category.products.all()

    # Render a template and pass the category to the context
    return render(request, 'single_category.html', {'category': category, 'products': products})
