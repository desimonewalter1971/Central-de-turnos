from django import forms

class medicosFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    matricula = forms.IntegerField()