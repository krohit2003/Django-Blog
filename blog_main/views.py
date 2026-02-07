from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Category, Blog

from assignments.models import About

from . import forms

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate
from django.contrib import auth


def home(request):

    featured_posts = Blog.objects.filter(is_featured=True, status="published")
    post = Blog.objects.filter(is_featured=False, status="published")

    try:
        about = About.objects.get()
    except:
        about = None

    context = {"featured_posts": featured_posts, "post": post, "about": about}

    return render(request, "home.html", context)


def register(request):

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
        else:
            print(form.errors)

    else:
        form = forms.RegisterForm()
    context = {"form": form}
    return render(request, "register.html", context)


def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("home")
        else:
            print("error")
            print(form.errors)

    form = AuthenticationForm()

    context = {"form": form}

    return render(request, "login.html", context)

def logout(request):
    auth.logout(request)
    return redirect('home')