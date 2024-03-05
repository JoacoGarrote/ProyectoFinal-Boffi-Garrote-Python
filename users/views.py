from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.forms import UsuarioEditForm, UsuarioRegisterForm
from users.models import Imagen
from django.contrib.auth.forms import AuthenticationForm

def iniciar_sesion(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("nombre_usuario")
            contrasena = form.cleaned_data.get("contrasena1")

            usuario_log = authenticate(nombre_usuario= usuario, contrasena1=contrasena)

            if usuario_log is not None:
                login(request, usuario_log)
                return render(request, "appentrega/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/iniciar_sesion.html", {"form": form, "msg_login": msg_login})

def registrar_usuario(request):
    msg_register = ""
    if request.method == 'POST':

        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"appentrega/index.html")
        
        msg_register = "Ha ingresado algún dato erróneo, por favor intentelo nuevamente."

    form = UsuarioRegisterForm()     
    return render(request,"users/registrar_sesion.html" ,  {"form":form, "msg_register": msg_register})

@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UsuarioEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            if informacion["contraseña"] != informacion["confirmacion"]:
                datos = {
                    "apellido": usuario.nombre,
                    "mail": usuario.mail
                }
                miFormulario = UsuarioEditForm(initial=datos)

            else:
                usuario.mail = informacion["mail"]
                if informacion["contraseña"]:
                    usuario.set_password(informacion["confirmacion"])
                usuario.nombre = informacion["nombre"]
                usuario.apellido = informacion["apellido"]
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
            "nombre": usuario.nombre,
            "mail": usuario.mail
        }
        miFormulario = UsuarioEditForm(initial=datos)

    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})

