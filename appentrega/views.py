from django.shortcuts import render, redirect
from django.urls import reverse
from appentrega.models import Empleado, Trabajo, Empresa
from appentrega.forms import FormTrabajo, FormEmpresa, BuscarEmpleado
# Create your views here.

def inicio(request):
    return render(request, "appentrega/index.html")

def empleados(request):
    return render(request, "appentrega/empleados.html")

def trabajos(request):
    return render(request, "appentrega/trabajos.html")

def empresas(request):
    return render(request, "appentrega/empresas.html")

def buscador(request):
    return render(request, "appentrega/buscador.html")


def form_empleados(request):
      
      if request.method == 'POST':

        empleado = Empleado(nombre=request.POST['nombre'],apellido=request.POST['apellido'],trabajo=request.POST['trabajo'])
 
        empleado.save()
 
        return render(request, "appentrega/index.html")
 
      return render(request,"appentrega/empleados.html")

def form_trabajos(request):
 
      if request.method == "POST":
 
            miFormulario = FormTrabajo(request.POST)
    
            if miFormulario.is_valid():
                  
                  informacion = miFormulario.cleaned_data
                  trabajo = Trabajo(rubro=informacion["rubro"], puesto=informacion["puesto"])
                  trabajo.save()
                  return render(request, "appentrega/index.html")
      else:
            miFormulario = FormTrabajo()
 
      return render(request, "appentrega/trabajos.html", {"miFormulario": miFormulario})

def form_empresas(request):
       
      if request.method == "POST":
 
            miFormulario = FormEmpresa(request.POST)
    
            if miFormulario.is_valid():
                  
                  informacion = miFormulario.cleaned_data
                  empresa = Empresa(nombre=informacion["nombre"], rubro=informacion["rubro"])
                  empresa.save()
                  return render(request, "appentrega/index.html")
      else:
            miFormulario = FormEmpresa()
 
      return render(request, "appentrega/empresas.html", {"miFormulario": miFormulario})


def buscar_empleados(request):
    empleados = Empleado.objects.all()

    if request.method == 'POST':
        form = BuscarEmpleado(request.POST)
        if form.is_valid():
            # Filtrar empleados según los campos del formulario
            nombre = form.cleaned_data.get('nombre', '')
            apellido = form.cleaned_data.get('apellido', '')
            trabajo = form.cleaned_data.get('trabajo', '')

            empleados = Empleado.objects.filter(
                nombre__icontains=nombre,
                apellido__icontains=apellido,
                trabajo__icontains=trabajo
            )
    else:
        # Mostrar todos los empleados si no hay búsqueda
        form = BuscarEmpleado()

    return render(request, 'appentrega/buscar_empleados.html', {'empleados': empleados, 'form': form})
