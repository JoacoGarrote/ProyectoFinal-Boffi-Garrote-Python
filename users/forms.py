from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UsuarioEditForm(UserCreationForm):
    mail = forms.EmailField(label="Por favor, ingrese su correo electrónico:")
    contrasena = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput, required=False)
    confirmacion = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput, required=False)

    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["nombre", "apellido", "mail", "contraseña", "confirmacion"]


class UsuarioRegisterForm(UserCreationForm):
    mail = forms.EmailField()
    contrasena = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput)
    confirmacion = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["usuario", "mail", "contraseña", "confirmacion"]