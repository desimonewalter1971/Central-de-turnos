from django.db import models
from datetime import datetime
 
class medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    servicio= models.CharField(max_length=40)
    matricula = models.IntegerField()
    def __str__(self):
        return (f"Dr/a {self.nombre} {self.apellido} - Servicio: {self.servicio} - Matricula N°: {self.matricula}")


class especialidades(models.Model):
    especialidad= models.CharField(max_length=40)
    def __str__(self):
        return (f"{self.especialidad}")
 
class pacientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    obraSocial = models.CharField(max_length=40)
    DNI=models.IntegerField()
    fechaNacimento = models.DateField()
    email=models.EmailField()
    
    def __str__(self):
        return (f"Nombre-Apellido: {self.nombre} {self.apellido} - Obra Social: {self.obraSocial} - DNI: {self.DNI} - Fecha Nacimiento: {self.fechaNacimento}")

class agenda(models.Model):
    medico= models.CharField(max_length=40)
    desde = models.DateTimeField('Dia / Desde hora', null=True ,  blank=True)
    hasta = models.TimeField('Hasta hora', null=True,  blank=True)
    
    def __str__(self):
        return (f"Nombre-Apellido: {self.medico} {self.desde} - Obra Social: {self.hasta}")
                
class turnos(models.Model):
    DNI=models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    medico= models.CharField(max_length=40)
    obraSocial = models.CharField(max_length=40)
    Dia = models.DateTimeField('Dia / horario', null=True ,  blank=True)
    
    def __str__(self):
        return (f"Paciente: {self.apellido} {self.nombre} - DNI: {self.DNI} - Prestador: {self.obraSocial} - Profesional: {self.medico} - dia: {self.Dia}")

    

    