from django import forms
from .models import especialidades

class medicosFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    Servicio=forms.ModelChoiceField( label= 'especialidad', queryset=especialidades.objects.all())
    matricula= forms.IntegerField()

class pacientesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    obraSocial= forms.CharField()
    DNI=forms.IntegerField()
    fecha_Nacimento= forms.DateField()    

class especialidadesFormulario(forms.Form):
    especialidad= forms.CharField()

class turnosFormularios(forms.Form):
    DNI=forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField
    medico= forms.CharField()
    obra_Social = forms.CharField()
    Dia = forms.DateTimeField()