from django.db import models


class medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    matricula = models.IntegerField()

class pacientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    obraSocial = models.CharField(max_length=40)
    fechaNacimento = models.DateField()

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

class Especialidades(models.Model):
    Especialidad = models.CharField(max_length=40)

    

    