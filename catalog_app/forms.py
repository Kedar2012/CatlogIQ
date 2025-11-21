from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ['name', 'description', 'price', 'sku_code', 'stock','category', 'image']
        
        widgets = {'description': forms.Textarea(attrs={'rows': 3}),}
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

