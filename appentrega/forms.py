from django import forms

class FormEmpleado(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    trabajo = forms.IntegerField()
    
class FormTrabajo(forms.Form):
    rubro = forms.CharField()
    puesto = forms.CharField()

class FormEmpresa(forms.Form):
    nombre = forms.CharField()
    rubro = forms.CharField()

class BuscarEmpleado(forms.Form):
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    trabajo = forms.CharField(required=False)