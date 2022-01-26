from email import message
from multiprocessing import context
from random import sample
from django.shortcuts import render, redirect

from .models import Appointment, Doctor, Opinion, STATUS_OF_VISIT
from .forms import AppointmentForm, DoctorForm, OpinionForm



def home(request):
    doctors =list(Doctor.objects.all())#pobieranie wszystkich lekarzy
    numberOfDoctors = len(doctors)
    if numberOfDoctors >= 3:
        doctors_3 = sample(doctors,3)# pobieranie 3 losowych lekarzy do wyświetlenia
    else:
        doctors_3 = sample(doctors, numberOfDoctors)
    if request.user.is_authenticated: # sprawdzenie czy użytkownik jest zalogowany i zwraca odpowiedni widok
        return render(request, 'home.html', {'doctors':doctors_3})
    else:
        return render(request, 'home_unauthenticated.html', {'doctors':doctors_3})


def opinions(request):
    opinions = Opinion.objects.all()
    context = {'opinions': opinions}
    if request.user.is_authenticated:
        return render(request, 'opinions.html', context)
    else:
        return render(request, 'opinions_unauthenticated.html', context)


def contact(request):
    return render(request, 'contact.html')

def appointment2(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.filter(created_by=request.user)#filtrowanie danych z bazy według użytkownika który wysłał zapytanie
        return render(request, 'myappointment.html', {'appointments':appointments})
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
    if request.user.is_authenticated:
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
    else:
        opinions = Opinion.objects.all()
        context = {'opinions': opinions}
        return render(request, 'opinions_unauthenticated.html', context)

def addAppointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        print(request.POST)
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated:
            obje = form.save(commit=False) #pobranie obiektu z formularza i przypisanie mu odpowiednich danych
            obje.created_by = request.user
            #obje.status = STATUS_OF_VISIT[0]
            #obje.status_of_visit = STATUS_OF_VISIT['Anulowana']
            obje.status_of_visit = 'Oczekuje na akceptacje'
            form.save()
    context = {'form':form}
    return render(request, 'addAppointment.html', context)

def cancelAppointment(request, id):
    if request.user.is_authenticated:
        try:
            appointment = Appointment.objects.get(id=id)#zwrócenie wizyt wizyt danego użytkownika
        except Appointment.DoesNotExist:
            return render(request, appointment2)
        if(appointment.created_by == request.user):
            appointment.status_of_visit = 'Anulowana'
            appointment.save()
            appointments = Appointment.objects.filter(created_by=request.user)
            return render(request, 'myappointment.html', {'appointments':appointments})
        else:
            appointments = Appointment.objects.filter(created_by=request.user)
            return render(request, 'myappointment.html', {'appointments':appointments})
    else:
        return render(request, 'home.html')
