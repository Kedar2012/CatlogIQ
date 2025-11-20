from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'users_app/register_user.html')
    else:
        form = RegisterForm()
    return render(request, 'users_app/register_user.html', {'form': form})