from django import forms

class medicosFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    matricula= forms.IntegerField()

class pacientesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    obraSocial= forms.CharField()
    fechaNacimento= forms.DateField()    