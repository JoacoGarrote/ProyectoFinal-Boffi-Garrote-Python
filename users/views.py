from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import UsuarioEditForm, UsuarioRegisterForm
from users.models import Imagen
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def iniciar_sesion(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return render(request, "appentrega/index.html")

        msg_login = "Usuario o contraseña incorrectos"
        
    form = AuthenticationForm()
    return render(request, "users/iniciar_sesion.html", {"form": form, "msg_login": msg_login})

def registrar_usuario(request):
    msg_register = ""
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "appentrega/index.html")
        else:
            msg_register = "Ha ingresado algún dato erróneo, por favor inténtelo nuevamente."

    form = UsuarioRegisterForm()     
    return render(request, "users/registrar_sesion.html", {"form": form, "msg_register": msg_register})

@login_required
# def editar_usuario(request):
#     usuario = request.user

#     if request.method == 'POST':
#         miFormulario = UsuarioEditForm(request.POST, request.FILES)

#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data

#             if informacion["password1"] != informacion["password2"]:
#                 datos = {
#                     "first_name": usuario.first_name,
#                     "email": usuario.email
#                 }
#                 miFormulario = UsuarioEditForm(initial=datos)
#             else:
#                 usuario.email = informacion["mail"]
#                 if informacion["contrasena"]:
#                     usuario.set_password(informacion["confirmacion"])
#                 usuario.first_name = informacion["first_name"]
#                 usuario.last_name = informacion["last_name"]
#                 usuario.save()

#                 try:
#                     avatar = Imagen.objects.get(user=usuario)
#                 except Imagen.DoesNotExist:
#                     avatar = Imagen(user=usuario, imagen=informacion["imagen"])
#                     avatar.save()
#                 else:
#                     avatar.imagen = informacion["imagen"]
#                     avatar.save()

#                 return render(request, "appentrega/index.html")

#     else:
#         datos = {
#             "first_name": usuario.first_name,
#             "email": usuario.email
#         }
#         miFormulario = UsuarioEditForm(initial=datos)

#     return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UsuarioEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    "first_name": usuario.first_name,
                    "email": usuario.email
                }
                miFormulario = UsuarioEditForm(initial=datos, instance=usuario)
            else:
                usuario.email = informacion["email"]
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.first_name = informacion["first_name"]
                usuario.last_name = informacion["last_name"]
                usuario.save()

                try:
                    avatar = Imagen.objects.get(user=usuario)
                except Imagen.DoesNotExist:
                    avatar = Imagen(user=usuario, imagen=informacion["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = informacion["imagen"]
                    avatar.save()

                return render(request, "appentrega/index.html")

    else:
        datos = {
            "first_name": usuario.first_name,
            "email": usuario.email
        }
        miFormulario = UsuarioEditForm(initial=datos, instance=usuario)

    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})

def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, "appentrega/index.html")