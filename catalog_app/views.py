from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm

# Create your views here.
def create_product(request):
    if request.user.Role != 'Vendor':
        return HttpResponseForbidden("Only vendors can add products.")
    
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