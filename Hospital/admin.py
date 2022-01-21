from django.contrib import admin
from .models import Appointment, Doctor, Opinion

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Opinion)
admin.site.register(Appointment)
