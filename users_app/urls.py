from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
]
