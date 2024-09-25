from django.shortcuts import render, get_object_or_404
from .models import Category  # Assuming you have a Category model


def category_detail(request):
    categories = Category.objects.all()
    return render(request,'category.html',{'categoreies':categories})

# def category_detail(request, id):
#     # Get the category based on the category_id
#     category = get_object_or_404(Category, id)
    
#     # Render a template and pass the category to the context
#     return render(request, 'category.html', {'category': category})
