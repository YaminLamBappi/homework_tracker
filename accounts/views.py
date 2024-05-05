from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileUpdateForm


def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})



@login_required
def home(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    return render(request, "home.html")


@csrf_exempt
def user_login(request):
    form = UserLoginForm() 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "home.html")
        else:
            form = UserLoginForm()  
            messages.error(request, "Login Credential Did not Match.")  
            return render(request, "login.html", {'form': form})
        
    return render(request, "login.html", {'form': form})



def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("user_login")
        else:
            form = UserRegistrationForm()
    return render(request, "signup.html",{
        "form": form
    })
        