from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.
def index(request):
    messages.success(request, "Login to our website")
    print(request.user)
    if request.user.is_anonymous:
        return render(request,"index.html")
        

    context = {
        "variable":"this is sent"
        }
    return render(request, 'index.html', context)
    

def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = User.objects.create_user(username,email, password)
        user.save()

        if user is not None:
            login(request ,user)
            return render(request, 'signup.html')
    # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return redirect('/')
    # return HttpResponse("This is login")

    return redirect('/')

def loginUser(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        # check if user has entered correct credentoials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request ,user)
            return render(request, 'login.html')
    # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return redirect('/')
    # return HttpResponse("This is login")

    return redirect('/')


def logoutUser(request):
    logout(request)
    return redirect("/")

