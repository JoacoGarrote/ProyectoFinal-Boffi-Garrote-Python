from django import forms

class CrearEvento(forms.Form):
    nombre = forms.CharField()
    fecha = forms.IntegerField()

class BuscarEvento(forms.Form):
    nombre = forms.TextInput()
