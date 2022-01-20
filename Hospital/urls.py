from django.urls import path
from . import views

#przekierowania do odpowiednich funkcji
urlpatterns = [
    path('home/', views.home, name='home'),
    path('opinions/', views.addOpinionForm, name='opinions'),
    path('visits/', views.visits, name='visits'),
    path('contact/', views.contact, name='contact'),
    path('myappointment/', views.appointment),
    path('addDoctor/', views.addDoctorForm),
    path('', views.home)
    
]