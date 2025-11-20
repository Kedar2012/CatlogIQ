from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
]
