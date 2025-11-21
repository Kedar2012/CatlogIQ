from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from users_app import forms

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['Password'])
            user.is_active = True
            user.save()
            return redirect('login_user')
    else:
        form = RegisterForm()
    return render(request, 'users_app/register_user.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.Role == "Customer":
                    return redirect('customer_dashboard')
                elif user.Role == "Vendor":
                    return redirect('home')
                else:
                    return redirect('home')
            else:
                form.add_error(None, "Invalid credentials")
            
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users_app/login_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')


def customer_dashboard(request):
    return render(request, 'users_app/customer_dashboard.html', {'role': request.user.Role})