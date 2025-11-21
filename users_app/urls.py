from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('vendor_dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
]
