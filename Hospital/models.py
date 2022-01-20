from sqlite3 import Timestamp
from django.db import models

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
        return self.firstname