from lib2to3.pgen2.token import OP
from django.forms import ModelForm
from .models import Doctor, Opinion

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        exclude = ['created_by'] 