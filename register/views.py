from django.shortcuts import render, redirect
from .forms import RegUser


def register(response):
    if response.method == "POST":
        form = RegUser(response.POST)
        if form.is_valid():
            form.save()
        #return redirect('/home')
    else:
        form = RegUser()

    return render(response, "registration/register.html", {"form":form})

def loginPage():
    return redirect('registration/login')