from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def home(request):
   return render (request,"home.html")
def login(request):
   return render (request,"login.html")
def inscription(request):
    return render (request,"register.html")
def info(request):
    return render (request,"info.html")
def budgetisation(request):
    return render (request,"budgetisation.html")

def custom_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context={'form': form}
    return render(request, 'register.html',context)