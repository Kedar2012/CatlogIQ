from django.db import models

from users_app.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'Role': 'Vendor'})
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku_code = models.CharField(max_length=50, unique=True)
    stock = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, related_name='products')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'Role': 'Customer'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"