from django.contrib import admin
from .models import Empleado, Trabajo, Empresa

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Trabajo)
admin.site.register(Empresa)

# SUPERUSUARIO:
# User - Joaco
# Password - 123