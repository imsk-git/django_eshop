from django.urls import path
from . import views


urlpatterns = [
    path('',views.admin_dashboard, name='admin_dashboard'),
    path('products/', views.products, name='admin_products'),
    path('products/add/', views.add_product, name='admin_add_product'),
    path('categories/add/', views.add_category, name='admin_add_category'),
    path('products/edit/<int:id>/', views.edit_product, name='admin_edit_product'),
    path('accounts/', views.accounts, name='admin_accounts'),
    path('login/', views.login, name='admin_login'),
    path('logout/', views.logout, name='logout'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_products'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),
]