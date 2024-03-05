from django.db import models

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
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
