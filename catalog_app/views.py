from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CategoryForm, ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, Category
# Create your views here.
def vendor_required(user):
    return user.Role == 'Vendor'

@login_required
@user_passes_test(vendor_required)
def create_product(request):   
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.save()
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()

    return render(request, 'catalog_app/create_product.html', {'form': form})

@login_required
@user_passes_test(vendor_required)
def view_my_products(request):
    user = request.user
    my_products = Product.objects.filter(vendor=user)
    return render(request, 'catalog_app/my_products.html', {
        'user': user,
        'my_products': my_products,
    })

@login_required
@user_passes_test(vendor_required)
def edit_product(request, pk):
    product = get_object_or_404(Product,pk=pk, vendor=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_my_products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'catalog_app/edit_product.html', {'form': form})

@login_required
@user_passes_test(vendor_required)
def delete_product(request, pk):
    product = get_object_or_404(Product,pk=pk, vendor=request.user)
    product.delete()
    return redirect('view_my_products')

def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'catalog_app/category_products.html', {
        'categories': categories
    })

def products_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'catalog_app/category_products.html', {
        'selected_category': category,
        'products': products,
        'categories': Category.objects.all(),  # for dropdown reuse
    })

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'catalog_app/cart.html', {'cart_items': cart_items})

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import Product, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')