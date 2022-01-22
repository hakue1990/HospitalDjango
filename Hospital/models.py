from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from functools import partial
from django import forms

from django.forms import DateInput

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

STATUS_OF_VISIT = [
        ('Anulowana','Anulowana'),
        ('Zaakceptowana','Zaakceptowana'),
        ('OczekujeNaAkceptacje','Oczekuje na akceptacje')
    ]

class Doctor(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True, verbose_name='Imie')
    lastname = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nazwisko')
    room = models.IntegerField(null=True, blank=True, default=0,verbose_name='Nr gabinetu')
    TYPE_OF_DOCTOR = [
        ('Chirurg','Chirurg'),
        ('Neurochirurg','Neurochirurg'),
        ('Kardiolog','Kardiolog'),
        ('Neurolog','Neurolog'),
        ('Okulista','Okulista'),
        ('Urolog','Urolog'),
        ('Alergolog','Alergolog'),
        ('Onkolog','Onkolog')
    ]
    typeofdoctor = models.CharField(max_length=50, null=True, blank=True, choices=TYPE_OF_DOCTOR, verbose_name='Specjalizacja')
    image = models.ImageField(null=True, blank=True, upload_to='imgs/')
    
    def __str__(self):
        return self.firstname +' '+ self.lastname + ' (' + self.typeofdoctor + ')'

class Opinion(models.Model):
    content = models.TextField(max_length=500, null=True, blank=True, verbose_name='Twoja opinia')
    opinion_for = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Wybierz lekarza')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Opinion For:" + self.opinion_for

class Appointment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, verbose_name='Wizyta u lekarza:')
    status_of_visit = models.CharField(max_length=20, null=True, blank=True, choices=STATUS_OF_VISIT)
    date_of_visit = models.DateTimeField(null=False, verbose_name='Termin wizyty')
    extra_info = models.TextField(max_length=200, null=True, blank=True, verbose_name='Dodatkowe informacje')
    