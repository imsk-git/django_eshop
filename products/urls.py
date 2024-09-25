from django.urls import path
from . import views

urlpatterns = [
    path('view-products/', views.product, name='product'),
    path('product-details/<int:id>/', views.single_product, name='productdetails'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-product/', views.add_product, name='add_product'),
]