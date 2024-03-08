from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Usuario, Anfitrion, Evento
from .forms import ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django import forms

# Create your views here.

def inicio(request):
    return render(request, "appentrega/index.html")

def about(request):
    return render(request, "appentrega/about.html")

def nada(request):
    return render(request, "appentrega/no_page.html")

# def filtrar_por_categoria(request, categoria):
#     eventos = Evento.objects.filter(categoria=categoria)
#     categorias = ["Sin categoría", "Festival Corporativo", "Festival Musical", "Festival Cine", "Festival Gastronomico", "Festival Deportivo"]

#     return render(request, "'appentrega/evento_lista.html", {'eventos': eventos, 'categorias': categorias})

# Usuario
class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    template_name = "appentrega/usuario_crear.html"
    fields = ["nombre", "apellido", "mail"]
    success_url = reverse_lazy("ListaUsuario")

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "appentrega/usuario/usuario_lista.html"

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = "appentrega/usuario/usuario_detalle.html"

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    success_url = reverse_lazy("ListaUsuario")
    fields = ["nombre", "apellido", "mail"]
    template_name = "appentrega/usuario/usuario_editar.html"

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy("ListaUsuario")
    template_name = 'appentrega/usuario/usuario_confdel.html'



# Anfitrion
class AnfitrionCreateView(LoginRequiredMixin, CreateView):
    model = Anfitrion
    template_name = "appentrega/anfitrion/anfitrion_crear.html"
    fields = ["nombre", "apellido", "mail"]
    success_url = reverse_lazy("ListaAnfitrion")

class AnfitrionListView(LoginRequiredMixin, ListView):
    model = Anfitrion
    template_name = "appentrega/anfitrion/anfitrion_lista.html"

class AnfitrionDetailView(LoginRequiredMixin, DetailView):
    model = Anfitrion
    template_name = "appentrega/anfitrion/anfitrion_detalle.html"

class AnfitrionUpdateView(LoginRequiredMixin, UpdateView):
    model = Anfitrion
    success_url = reverse_lazy("ListaAnfitrion")
    fields = ["nombre", "apellido", "mail"]
    template_name = "appentrega/anfitrion/anfitrion_editar.html"

class AnfitrionDeleteView(LoginRequiredMixin, DeleteView):
    model = Anfitrion
    success_url = reverse_lazy("ListaAnfitrion")
    template_name = 'appentrega/anfitrion/anfitrion_confdel.html'



# Eventos

class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    template_name = "appentrega/evento/evento_crear.html"
    fields = ["nombre", "categoria", "ubicacion", "fecha", "descripcion", "imagen"]
    success_url = reverse_lazy("ListaEvento")
    login_url = reverse_lazy("Nada")

    widgets = {
        "categoria": forms.Select(attrs={'class': 'form-control'}),
    }

class EventoListView(ListView):
    model = Evento
    template_name = "appentrega/evento/evento_lista.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EventoDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Evento
    template_name = "appentrega/evento/evento_detalle.html"
    form_class = ComentarioForm

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.evento = self.get_object()
        form.instance.usuario = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentario_form'] = self.get_form()
        return context


class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    success_url = reverse_lazy("ListaEvento")
    fields = ["nombre", "categoria", "ubicacion", "fecha", "descripcion", "imagen"]
    template_name = "appentrega/evento/evento_editar.html"


class EventoDeleteView(LoginRequiredMixin, DeleteView):
    model = Evento
    success_url = reverse_lazy("ListaEvento")
    template_name = 'appentrega/evento/evento_confdel.html'



# Categorias
    
# gastronomicos
def gastronomicos(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/gastronomicos.html", {'object_list': object_list})

# corporativos
def corporativos(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/corporativos.html", {'object_list': object_list})

# musicales
def musicales(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/musicales.html", {'object_list': object_list})

# cineastas
def cineastas(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/cineastas.html", {'object_list': object_list})

#deportivos
def deportivos(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/deportivos.html", {'object_list': object_list})

#sin categoria
def sin_categoria(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/sin_categoria.html", {'object_list': object_list})