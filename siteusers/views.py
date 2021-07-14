from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import MyUserCreationForm
from django.urls import reverse
# Create your views here.


def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": MyUserCreationForm}
        )

    elif request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
