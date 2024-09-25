from django.urls import path
from . import views

urlpatterns = [
    path('view-categories/', views.category_detail, name='category'),
    # path('categories-details/<str:name>/', views.category_detail, name='category_detail'),
]