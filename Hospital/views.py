from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import DoctorForm



def home(request):
    return render(request, 'home.html')

def opinions(request):
    return render(request, 'opinions.html')

def visits(request):
    return render(request, 'visits.html')

def contact(request):
    return render(request, 'contact.html')

def appointment(request):
    if request.user.is_authenticated:
        return render(request, 'myappointment.html', {})
    else:
        return redirect('/home')

def addDoctorForm(request):
    form = DoctorForm()
    if request.method == 'POST':
        print(request.POST)
        form= DoctorForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'addDoctor.html', context)