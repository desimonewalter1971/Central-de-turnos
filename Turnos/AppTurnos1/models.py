from django.db import models


class medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    matricula = models.IntegerField()
    def __str__(self):
        return (f"Dr/a {self.nombre} {self.apellido} - Matricula N°: {self.matricula}")


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
    def __str__(self):
        return (f"Nombre-Apellido: {self.nombre} {self.apellido} - Obra Social: {self.obraSocial} - DNI: {self.DNI} - Fecha Nacimiento: {self.fechaNacimento}")

class agendaDisponiblePorMedico(models.Model):
    medico= models.CharField(max_length=40)
    horario = models.DateTimeField()
    tarde_mañana = models.DateField()

class turnoReservado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    medico= models.CharField(max_length=40)
    obraSocial = models.CharField(max_length=40)
    Dia = models.DateField()

    

    