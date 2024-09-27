from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('category-details/<int:id>/', views.category_detail, name='category_detail'),
    # path('single-category/<int:id>/', views.single_category, name='single_category'),
]