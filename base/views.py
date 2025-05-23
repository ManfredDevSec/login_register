from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
      
 
    context={

    }
    return render(request, 'base/home.html', context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'base/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            return render(request, 'base/register.html', {'error' : 'Passwords do no match'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'base/register.html', {'error': 'Username or Password already taken'})
        
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        #login the user
        login(request, user)
        
        return render(request, 'base/register.html', { 'success': 'Account created successfully!'})
    
    return render(request, 'base/register.html')

def logout_view(request):
    logout(request)
    
    return redirect('login')

@login_required
def dashboard_view(request):
    context={

        
    }
    return render(request, 'base/dashboard.html', context)