from sqlite3 import Timestamp
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    room = models.IntegerField(null=True, blank=True, default=0)
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
    typeofdoctor = models.CharField(max_length=50, null=True, blank=True, choices=TYPE_OF_DOCTOR)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.firstname +' '+ self.lastname + ' (' + self.typeofdoctor + ')'

class Opinion(models.Model):
    content = models.TextField(max_length=500, null=True, blank=True, verbose_name='Twoja opinia')
    opinion_for = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Wybierz lekarza')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)