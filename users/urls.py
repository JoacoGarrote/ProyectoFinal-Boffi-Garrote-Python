from users import views
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path('iniciar_sesion/', views.iniciar_sesion, name="IniciarSesion"),
    path('cerrar_sesion/', views.cerrar_sesion, name="CerrarSesion"),
    path('registrar_usuario/', views.registrar_usuario, name="RegistrarUsuario"),
    path('editar_usuario/', views.editar_usuario, name="UsuarioEditar")
]
