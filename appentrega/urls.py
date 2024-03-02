from django.urls import path
from appentrega import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('empleados/', views.form_empleados, name="FormEmpleado"),
    path('buscar-empleados/', views.buscar_empleados, name="BuscarEmpleados"),
    path('trabajos/', views.form_trabajos, name="FormTrabajo"),
    path('empresas/', views.form_empresas, name="FormEmpresa")
]

