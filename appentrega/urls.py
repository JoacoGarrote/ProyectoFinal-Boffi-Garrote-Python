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
    path('eventos/', views.eventos, name="Eventos"),
    path('contacto/', views.contacto, name="Contacto"),
    path('acerca/', views.acerca, name="AcercaDe"),
]

#Usuario
urlpatterns += [
    path('usuario_crear/', views.UsuarioCreateView.as_view(), name="CrearUsuario"),
    path('usuario_lista/', views.UsuarioListView.as_view(), name="ListaUsuario"),
    path('usuario_detalle/<int:pk>/', views.UsuarioDetailView.as_view(), name="DetalleUsuario"),
    path('usuario_editar/<int:pk>/', views.UsuarioUpdateView.as_view(), name="EditarUsuario"),
    path('usuario_eliminar/<int:pk>/', views.UsuarioDeleteView.as_view(), name="EliminarUsuario"),
]

#Anfitrion
urlpatterns += [
    path('anfitrion_crear/', views.AnfitrionCreateView.as_view(), name="CrearAnfitrion"),
    path('anfitrion_lista/', views.AnfitrionListView.as_view(), name="ListaAnfitrion"),
    path('anfitrion_detalle/<int:pk>/', views.AnfitrionDetailView.as_view(), name="DetalleAnfitrion"),
    path('anfitrion_editar/<int:pk>/', views.AnfitrionUpdateView.as_view(), name="EditarAnfitrion"),
    path('anfitrion_eliminar/<int:pk>/', views.AnfitrionDeleteView.as_view(), name="EliminarAnfitrion"),
]
#Eventos
urlpatterns += [
    path('evento_crear/', views.EventoCreateView.as_view(), name="CrearEvento"),
    path('evento_lista/', views.EventoListView.as_view(), name="ListaEvento"),
    path('evento_detalle/<int:pk>/', views.EventoDetailView.as_view(), name="DetalleEvento"),
    path('evento_editar/<int:pk>/', views.EventoUpdateView.as_view(), name="EditarEvento"),
    path('evento_eliminar/<int:pk>/', views.EventoDeleteView.as_view(), name="EliminarEvento"),
]