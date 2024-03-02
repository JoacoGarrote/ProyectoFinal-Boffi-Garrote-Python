from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    trabajo = models.CharField(max_length=40)
    

class Trabajo(models.Model):
    rubro = models.CharField(max_length=40)
    puesto = models.CharField(max_length=20)
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=30)
    rubro = models.CharField(max_length=40)

