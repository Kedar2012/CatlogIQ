from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'),
    path('view_my_products/', views.view_my_products, name='view_my_products'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('categories/', views.list_categories, name='list_categories'),
    path('categories/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
