from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Usuario, Anfitrion, Evento
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from users.models import Imagen
from django import forms

# Create your views here.

def inicio(request):
    return render(request, "appentrega/index.html")

def contacto(request):
    return render(request, "appentrega/contacto.html")

def about(request):
    return render(request, "appentrega/about.html")

def nada(request):
    return render(request, "appentrega/no_page.html")

#Login Required -- Vistas basadas en clases:
# @login_required
def eventos(request):
    return render(request, "appentrega/eventos.html")

# Usuario
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
    template_name = "appentrega/usuario_detalle.html"

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    success_url = reverse_lazy("ListaUsuario")
    fields = ["nombre", "apellido", "mail"]
    template_name = "appentrega/usuario_editar.html"

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy("ListaUsuario")
    template_name = 'appentrega/usuario_confdel.html'



# Anfitrion
class AnfitrionCreateView(LoginRequiredMixin, CreateView):
    model = Anfitrion
    template_name = "appentrega/anfitrion_crear.html"
    fields = ["nombre", "apellido", "mail"]
    success_url = reverse_lazy("ListaAnfitrion")

class AnfitrionListView(LoginRequiredMixin, ListView):
    model = Anfitrion
    template_name = "appentrega/anfitrion_lista.html"

class AnfitrionDetailView(LoginRequiredMixin, DetailView):
    model = Anfitrion
    template_name = "appentrega/anfitrion_detalle.html"

class AnfitrionUpdateView(LoginRequiredMixin, UpdateView):
    model = Anfitrion
    success_url = reverse_lazy("ListaAnfitrion")
    fields = ["nombre", "apellido", "mail"]
    template_name = "appentrega/anfitrion_editar.html"

class AnfitrionDeleteView(LoginRequiredMixin, DeleteView):
    model = Anfitrion
    success_url = reverse_lazy("ListaAnfitrion")
    template_name = 'appentrega/anfitrion_confdel.html'



# Eventos
class EventoCreateView( CreateView):
    model = Evento
    template_name = "appentrega/evento_crear.html"
    fields = ["nombre", "categoria", "ubicacion", "fecha", "descripcion"]
    success_url = reverse_lazy("ListaEvento")
    widgets = {
        "categoria": forms.Select(attrs={'class': 'form-control'}),
    }

class EventoListView(ListView):
    model = Evento
    template_name = "appentrega/evento_lista.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EventoDetailView(LoginRequiredMixin, DetailView):
    model = Evento
    template_name = "appentrega/evento_detalle.html"

class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    success_url = reverse_lazy("ListaEvento")
    fields = ["nombre", "categoria", "ubicacion", "fecha", "descripcion"]
    template_name = "appentrega/evento_editar.html"

class EventoDeleteView(LoginRequiredMixin, DeleteView):
    model = Evento
    success_url = reverse_lazy("ListaEvento")
    template_name = 'appentrega/evento_confdel.html'