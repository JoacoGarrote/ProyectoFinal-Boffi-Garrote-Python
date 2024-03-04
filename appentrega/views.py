from django.shortcuts import render, redirect
from django.urls import reverse
from appentrega.models import Empleado, Trabajo, Empresa
from appentrega.forms import FormTrabajo, FormEmpresa, BuscarEmpleado
# Create your views here.

def inicio(request):
    return render(request, "appentrega/index.html")

def evento(request):
    return render(request, "appentrega/evento.html")

def contacto(request):
    return render(request, "appentrega/contacto.html")

def acerca(request):
    return render(request, "appentrega/acerca_de.html") 

