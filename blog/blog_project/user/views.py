from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

# Create your views here.
def inde(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'blog/home.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'user/login.html')        
            
    return render(request, 'user/login.html')

def userlogout(request):
    logout(request)
    return redirect('/login')