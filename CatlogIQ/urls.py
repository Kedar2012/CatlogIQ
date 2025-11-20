from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name='home'),
    path('Accounts/', include('users_app.urls')),
    path('Products/', include('catalog_app.urls')),
]
