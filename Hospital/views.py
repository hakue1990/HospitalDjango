from email import message
from multiprocessing import context
from random import sample
from django.shortcuts import render, redirect

from .models import Doctor, Opinion
from .forms import DoctorForm, OpinionForm



def home(request):
    doctors =list(Doctor.objects.all())
    numberOfDoctors = len(doctors)
    if numberOfDoctors >= 3:
        doctors_3 = sample(doctors,3)
    else:
        doctors_3 = sample(doctors, numberOfDoctors)
    if request.user.is_authenticated:
        return render(request, 'home.html', {'doctors':doctors_3})
    else:
        return render(request, 'home_unauthenticated.html', {'doctors':doctors_3})
        

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
        if form.is_valid() and request.user.is_superuser:
            form.save()
    context = {'form':form}
    if(request.user.is_superuser):
        return render(request, 'addDoctor.html', context)
    else:
        return redirect('/home')

def addOpinionForm(request):
    form = OpinionForm()
    opinions = Opinion.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = OpinionForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            obje = form.save(commit=False)
            obje.created_by = request.user
            form.save()
    context = {'form':form, 'opinions': opinions}
    return render(request, 'opinions.html', context)