from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserEditForm

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
            return redirect("appentrega/index.html")
    else:
        form = UserEditForm(instance=user)

    return render(request, 'users/editar_usuario.html', {'form': form})