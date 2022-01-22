from django.urls import path
from . import views
from register import views as regViews

#przekierowania do odpowiednich funkcji
urlpatterns = [
    path('home/', views.home, name='home'),
    path('opinions/', views.addOpinionForm, name='opinions'),
    path('visits/', views.visits, name='visits'),
    path('contact/', views.contact, name='contact'),
    path('myappointment/', views.appointment2),
    path('addDoctor/', views.addDoctorForm),
    path('addAppointment/', views.addAppointment),
    path('myappointment/cancel/<int:id>/', views.cancelAppointment),
    path('', views.home)
]