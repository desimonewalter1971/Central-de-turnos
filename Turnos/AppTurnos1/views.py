from django.shortcuts import render
from django.http import HttpResponse

def medicos (request):
    return HttpResponse('vista medicos')

def pacientes (request):
    return HttpResponse('vista pacientes')

def agendaDisponiblePorMedico (request):
    return HttpResponse('vista agendaDisponiblePorMedico')

def turnoReservado (request):
    return HttpResponse('vista turnoReservado')            
