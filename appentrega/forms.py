from django import forms
from .models import Comentario, Evento


#AGREGADO
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["nombre", "categoria", "ubicacion", "fecha", "descripcion", "imagen"]

        widgets = {
            "categoria": forms.Select(attrs={'class': 'form-control'}),
            "fecha": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }