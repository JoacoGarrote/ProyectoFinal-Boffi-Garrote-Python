from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserEditForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,"appentrega/index.html")
    else:
        form = RegistrationForm()
    
    return render(request, "users/registrar_usuario.html", {'form': form})

def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, "appentrega/index.html")


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "appentrega/index.html")
    
    else:
        form = AuthenticationForm()
    
    return render(request, "users/iniciar_sesion.html", {'form': form})

@login_required
def editar_usuario(request):
    user = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'users/editar_usuario.html')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'users/editar_usuario.html', {'form': form})

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.user
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            return render(request, 'users/editar_usuario.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/cambiar_contrasena.html', {'form': form})