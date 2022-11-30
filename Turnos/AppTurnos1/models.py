from django.db import models


class medicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    matricula = models.IntegerField()

class pacientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    Dia = models.CharField(max_length=40)
    fechaNacimento = models.IntegerField()

class agendaDisponiblePorMedico(models.Model):
    horario = models.CharField(max_length=40)
    tarde_mañana = models.CharField(max_length=40)

class paciturnoReservado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    Dia = models.CharField(max_length=40)
    fechaNacimento = models.IntegerField()    
    

    