from django import forms
from .models import especialidades, medicos, pacientes, agenda

class medicosFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    matricula= forms.IntegerField()
    Servicio_id= forms.ModelChoiceField( label= 'Especialidad', queryset=especialidades.objects.all())

class pacientesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    obraSocial= forms.CharField()
    DNI=forms.IntegerField()
    fecha_Nacimento= forms.DateField(label='Ingrese su fecha de nacimiento.')         

class especialidadesFormulario(forms.Form):
    especialidad= forms.CharField(label= 'Cargar Especialidad')

class turnosFormularios(forms.Form):
    agendas=forms.ModelChoiceField( label= 'Agenda', queryset=agenda.objects.all())
    paciente= forms.ModelChoiceField( label= 'paciente', queryset=pacientes.objects.all())
    #obra_Social = forms.CharField()
    Dia = forms.DateTimeField()    
    
class agendaFormularios(forms.Form):  
    profesional= forms.ModelChoiceField( label= 'Profesional', queryset=medicos.objects.all())
    desde = forms.DateTimeField()
    hasta = forms.TimeField()     