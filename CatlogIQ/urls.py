from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name='home'),
    path('Accounts/', include('users_app.urls')),
    path('Products/', include('catalog_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

