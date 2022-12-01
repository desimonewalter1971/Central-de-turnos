from django.shortcuts import render
from django.http import HttpResponse

from AppTurnos1.models import medicos as mc
from django.core import serializers


def inicio (request):
    return render(request,'AppTurnos1/inicio.html')

def medicos (request):
    return render(request,'AppTurnos1/medicos.html')

def medicosapi (request):
    todos_medicos=mc.objects.all()
    return HttpResponse(serializers.serialize('json', todos_medicos))    

def pacientes (request):
    return render(request,'AppTurnos1/pacientes.html')

def agendaDisponiblePorMedico (request):
    return render('AppTurnos1/agendaDisponiblePorMedico.html')

def turnoReservado (request):
    return render('AppTurnos1/turnoReservado.html')            
