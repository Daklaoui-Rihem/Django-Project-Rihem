from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def home(request):
    return render(request, "home.html")



def authView(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("base:home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" :form})

def loginu(request):
    if request.method== "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("base:home")
    else:
       form = AuthenticationForm()
    return render(request, "registration/login.html", {"form" :form})