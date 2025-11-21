from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm, LoginForm, UserUpdateForm, UserProfileUpdateForm
from .models import UserProfile

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
        login_type = request.POST.get('login_type')

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.Role == "Customer" and login_type == 'customer':
                    login(request, user)
                    return redirect('customer_dashboard')
                elif user.Role == "Vendor" and login_type == 'vendor':
                    login(request, user)
                    return redirect('vendor_dashboard')
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

def vendor_required(user):
    return user.Role == 'Vendor'

def customer_required(user):
    return user.Role == 'Customer'

@login_required
@user_passes_test(customer_required)
def customer_dashboard(request):
    return render(request, 'users_app/customer_dashboard.html', {'role': request.user.Role})

@login_required
@user_passes_test(vendor_required)
def vendor_dashboard(request):
    return render(request, 'users_app/vendor_dashboard.html', {'role': request.user.Role})


@login_required
def view_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    context = {
        'user': user,
        'profile': user_profile,
    }
    return render(request, "users_app/view_profile.html", context)


@login_required
def edit_profile(request):
    if request.user.Role == "Admin":
        return HttpResponseForbidden("Admins must use the admin panel to edit profiles.")

    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("view_profile")
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UserProfileUpdateForm(instance=profile)

    return render(request, "users_app/edit_profile.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })

