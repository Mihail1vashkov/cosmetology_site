from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Doctor, Service, Procedure

def index(request):
    return render(request, 'cosmetology/index.html')

def doctors(request):
    doctors = Doctor.objects.all() # Получаем всех врачей из базы данных
    return render(request, 'cosmetology/doctors.html', {'doctors': doctors})

def services(request):
    services = Service.objects.all() # Получаем список услуг из базы данных
    return render(request, 'cosmetology/services.html', {'services': services})

def procedures(request):
    procedures = Procedure.objects.all()# Получаем список процедур из базы данных
    return render(request, 'cosmetology/procedures.html', {'procedures': procedures})
