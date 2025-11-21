from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_user')
def Home(request):
    context = {
        "user": request.user,
        "role": request.user.Role,   # custom field from your model
    }

    return render(request, 'home.html', context)