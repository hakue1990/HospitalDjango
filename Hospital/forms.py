from lib2to3.pgen2.token import OP
from django.forms import ModelForm
from django import forms
from .models import Appointment, Doctor, Opinion
from django.contrib.admin.widgets import AdminDateWidget

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        exclude = ['created_by'] 

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ['created_by', 'status_of_visit']
        date_of_visit = forms.DateField(widget=AdminDateWidget())