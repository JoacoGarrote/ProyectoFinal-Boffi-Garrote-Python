from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Evento, Comentario
from .forms import ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import EventoForm

# Create your views here.

def inicio(request):
    return render(request, "appentrega/index.html")

def about(request):
    return render(request, "appentrega/about.html")

def no_page(request):
    return render(request, "appentrega/no_page.html")

def login_requerido(request):
    return render(request, "appentrega/login_requerido.html")


# Eventos

class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    template_name = "appentrega/evento/evento_crear.html"
    form_class = EventoForm
    success_url = reverse_lazy("ListaEvento")
    login_url = reverse_lazy("LoginRequerido")

class EventoListView(ListView):
    model = Evento
    template_name = "appentrega/evento/evento_lista.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EventoDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Evento
    template_name = "appentrega/evento/evento_detalle.html"
    form_class = ComentarioForm
    login_url = reverse_lazy("LoginRequerido")

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
    login_url = reverse_lazy("LoginRequerido")
    template_name = "appentrega/evento/evento_editar.html"


class EventoDeleteView(LoginRequiredMixin, DeleteView):
    model = Evento
    success_url = reverse_lazy("ListaEvento")
    template_name = 'appentrega/evento/evento_confdel.html'



# Categorias
    
# Gastronomicos

def gastronomicos(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/gastronomicos.html", {'object_list': object_list})


# Corporativos

def corporativos(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/corporativos.html", {'object_list': object_list})

# Musicales

def musicales(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/musicales.html", {'object_list': object_list})

# Cineastas

def cineastas(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/cineastas.html", {'object_list': object_list})

# Deportivos

def deportivos(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/deportivos.html", {'object_list': object_list})

# Sin categoria

def sin_categoria(request):
    object_list = Evento.objects.all()
    return render(request, "appentrega/evento/categorias/sin_categoria.html", {'object_list': object_list})

# Comentario
class EliminarComentarioView(View):
    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        comentario.delete()
        return redirect(request.META.get('HTTP_REFERER'))


