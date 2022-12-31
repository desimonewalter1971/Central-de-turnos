from django.db import models
from datetime import datetime
 
 

class especialidades(models.Model):
    especialidad= models.CharField(max_length=40)
    def __str__(self):
        return (f"{self.especialidad}")    

class medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    servicio= models.CharField(max_length=40)
    matricula = models.IntegerField()
    def __str__(self):
        return (f"Dr/a {self.nombre} {self.apellido} - Servicio: {self.servicio} - Matricula N°: {self.matricula}")
   
 
class pacientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    obraSocial = models.CharField(max_length=40)
    DNI=models.IntegerField()
    fecha_Nacimento = models.DateField()
    email=models.EmailField()
    
    def __str__(self):
        return (f" {self.nombre} {self.apellido} - Obra Social: {self.obraSocial} - DNI: {self.DNI} - Fecha Nacimiento: {self.fecha_Nacimento}")


class agendas(models.Model):
    medico= models.CharField(max_length=40)
    desde = models.DateTimeField('Dia / Desde hora', null=True ,  blank=True)
    hasta = models.TimeField('Hasta hora', null=True,  blank=True)
    
    def __str__(self):
        return (f" {self.medico} - Turno Hora: {self.hasta}")
                
              
class turnos(models.Model):
    DNI=models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    medico= models.CharField(max_length=40)
    obraSocial = models.CharField(max_length=40)
    Dia = models.DateTimeField('Dia / horario', null=True ,  blank=True)
    
    def __str__(self):
        return (f"Paciente: {self.apellido} {self.nombre} - DNI: {self.DNI} - Prestador: {self.obraSocial} - Profesional: {self.medico} - dia: {self.Dia}")

 


 

   

 

    
    