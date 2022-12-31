from django import forms
from .models import especialidades, medicos, pacientes, agendas

class medicosFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    matricula= forms.IntegerField()
    Servicio=forms.ModelChoiceField( label= 'Especialidad', queryset=especialidades.objects.all())

class pacientesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    obraSocial= forms.CharField()
    DNI=forms.IntegerField()
    fecha_Nacimento= forms.DateField()         

class especialidadesFormulario(forms.Form):
    especialidad= forms.CharField()

class turnosFormularios(forms.Form):
    agendas=forms.ModelChoiceField( label= 'Agenda', queryset=agendas.objects.all())
    paciente= forms.ModelChoiceField( label= 'paciente', queryset=pacientes.objects.all())
    #obra_Social = forms.CharField()
    Dia = forms.DateTimeField()    
    
class agendaFormularios(forms.Form):  
    profesional= forms.ModelChoiceField( label= 'Profesional', queryset=medicos.objects.all())
    desde = forms.DateTimeField()
    hasta = forms.TimeField()     