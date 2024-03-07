from django.db import models
from users.models import CustomUser

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    
class Anfitrion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)

class Evento(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=10000)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    evento = models.ForeignKey(Evento, related_name='comentarios', on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return f'{self.usuario.username} - {self.mensaje}'
