from django.urls import path
from appentrega import views

# urlpatterns = [
#     path('', views.inicio, name="Inicio"),
#     path('empleados/', views.form_empleados, name="FormEmpleado"),
#     path('buscar-empleados/', views.buscar_empleados, name="BuscarEmpleados"),
#     path('trabajos/', views.form_trabajos, name="FormTrabajo"),
#     path('empresas/', views.form_empresas, name="FormEmpresa"),
#     path('prueba/', views.ricardo, name="Ricardo"),
# ]

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('evento/', views.inicio, name="Evento"),
    path('contacto/', views.contacto, name="Contacto"),
    path('acerca/', views.acerca, name="AcercaDe"),
]

