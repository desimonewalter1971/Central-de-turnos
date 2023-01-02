from django.db import models
from datetime import datetime
 
class medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    servicio= models.ForeignKey("AppTurnos1.especialidades", on_delete=models.CASCADE)
    matricula = models.IntegerField()
    def __str__(self):
        return (f"Dr/a {self.nombre} {self.apellido} - Servicio de: {self.servicio} - Matricula N°: {self.matricula}")


class especialidades(models.Model):
    especialidad= models.CharField(max_length=40)
    def __str__(self):
        return (f"{self.especialidad}")
 
class pacientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    obraSocial = models.CharField(max_length=40)
    DNI=models.IntegerField()
    fecha_Nacimento = models.DateField()
    email=models.EmailField()
    
    def __str__(self):
        return (f"Nombre-Apellido: {self.nombre} {self.apellido} - Obra Social: {self.obraSocial} - DNI: {self.DNI} - Fecha Nacimiento: {self.fecha_Nacimento}")

class agenda(models.Model):
    medico= models.OneToOneField("AppTurnos1.medicos", on_delete=models.CASCADE)
    desde = models.DateTimeField('Dia / Desde hora', null=True ,  blank=True)
    hasta = models.TimeField('Hasta hora', null=True,  blank=True)
    
    def __str__(self):
        return (f"Nombre-Apellido: {self.medico} {self.desde} - Obra Social: {self.hasta}")
                
class turnos(models.Model):
    agenda=models.OneToOneField("AppTurnos1.agenda", on_delete=models.CASCADE)
    paciente= models.OneToOneField("AppTurnos1.pacientes", on_delete=models.CASCADE)
   
    
    def __str__(self):
        return (f"Paciente: {self.paciente.nombre} {self.paciente.apellido} - DNI: {self.paciente.DNI} - Prestador: {self.agenda}")

    

    