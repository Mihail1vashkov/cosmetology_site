from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.doctors, name='doctors'),
    path('services/', views.services, name='services'),
    path('procedures/', views.procedures, name='procedures'),
]
