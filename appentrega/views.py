from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Usuario, Anfitrion, Evento
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, "appentrega/index.html")

def contacto(request):
    return render(request, "appentrega/contacto.html")

def acerca(request):
    return render(request, "appentrega/acerca_de.html") 

#Login Required -- Vistas basadas en clases:
# @login_required
def eventos(request):
    return render(request, "appentrega/eventos.html")

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    template_name = "appentrega/usuario_crear.html"
    fields = ["nombre", "apellido", "mail"]
    success_url = reverse_lazy("ListaUsuario")

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "appentrega/usuario_lista.html"

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = "appcoder/usuario_detalle.html"

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    success_url = reverse_lazy("ListaUsuario")
    fields = ["nombre", "apellido", "mail"]
    template_name = "AppCoder/usuario_editar.html"

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy("ListaUsuario")
    template_name = 'AppCoder/usuario_confdel.html'