from django import forms

class BuscarEvento(forms.Form):
    nombre = forms.CharField()
    fecha = forms.IntegerField()
