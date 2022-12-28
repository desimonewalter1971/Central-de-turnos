from django import forms
from .models import especialidades

class medicosFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    especialidad=forms.ModelChoiceField( label= 'especialidad', queryset=especialidades.objects.all())
    matricula= forms.IntegerField()

class pacientesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    obraSocial= forms.CharField()
    DNI=forms.IntegerField()
    fechaNacimento= forms.DateField()    

class especialidadesFormulario(forms.Form):
    especialidad= forms.CharField()

