from django import forms
from .models import Comentario

class CrearEvento(forms.Form):
    nombre = forms.CharField()
    fecha = forms.IntegerField()

class BuscarEvento(forms.Form):
    nombre = forms.TextInput()

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }