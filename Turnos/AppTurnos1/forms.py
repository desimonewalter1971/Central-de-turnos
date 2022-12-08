from django import forms

class medicosFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    matricula= forms.IntegerField()

class pacientesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    obraSocial= forms.CharField()
    DNI=forms.IntegerField()
    fechaNacimento= forms.DateField()    

class especialidadesFormulario(forms.Form):
    especialidad= forms.CharField()

