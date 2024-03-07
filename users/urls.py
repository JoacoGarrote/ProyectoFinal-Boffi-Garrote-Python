from users import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('iniciar_sesion/', views.iniciar_sesion, name="IniciarSesion"),
    path('cerrar_sesion/', views.cerrar_sesion, name="CerrarSesion"),
    path('registrar_usuario/', views.registrar_usuario, name="RegistrarUsuario"),
    path('editar_usuario/', views.editar_usuario, name="UsuarioEditar"),
    path("cambiar_contrasena/", views.cambiar_contrasena, name="CambiarContrasena")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
