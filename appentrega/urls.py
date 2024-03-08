from django.urls import path
from appentrega import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import filtrar_por_categoria


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About"),
    path('no_page/', views.no_page, name="NoPage"),
    path('login_requerido/', views.login_requerido, name="LoginRequerido")
]

#Eventos
urlpatterns += [
    path('evento_crear/', views.EventoCreateView.as_view(), name="CrearEvento"),
    path('evento_lista/', views.EventoListView.as_view(), name="ListaEvento"),
    path('evento_detalle/<int:pk>/', views.EventoDetailView.as_view(), name="DetalleEvento"),
    path('evento_editar/<int:pk>/', views.EventoUpdateView.as_view(), name="EditarEvento"),
    path('evento_eliminar/<int:pk>/', views.EventoDeleteView.as_view(), name="EliminarEvento"),
    path('eliminar-comentario/<int:comentario_id>/', views.EliminarComentarioView.as_view(), name="EliminarComentario"),
]

#Categorias
urlpatterns += [
    path('gastronomicos/', views.gastronomicos, name="Gastronomicos"),
    path('corporativos/', views.corporativos, name="Corporativos"),
    path('musicales/', views.musicales, name="Musicales"),
    path('cineastas/', views.cineastas, name="Cineastas"),
    path('deportivos/', views.deportivos, name="Deportivos"),
    path('sin_categoria/', views.sin_categoria, name="Sin_categoria"),
    # path('eventos/categoria/<str:categoria>/', views.eventos_por_categoria, name='eventos_por_categoria'),
]

#Imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)