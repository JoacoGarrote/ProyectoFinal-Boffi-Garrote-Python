from django.db import models
from users.models import CustomUser
from django.utils import timezone
import pytz

# Create your models here.


class Evento(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=10000)
    imagen = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    evento = models.ForeignKey(Evento, related_name='comentarios', on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        zona_horaria_local = pytz.timezone('America/Argentina/Buenos_Aires')

        if not self.fechaComentario:
            self.fechaComentario = timezone.now()

        self.fechaComentario = timezone.localtime(self.fechaComentario, zona_horaria_local)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return f'{self.usuario.username} - {self.mensaje}'
