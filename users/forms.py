from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class UsuarioEditForm(UserChangeForm):
    email = forms.EmailField(label="Por favor, ingrese su correo electrónico:")
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class UsuarioRegisterForm(UserChangeForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']