from django.shortcuts import render
from django.http import HttpResponse

from AppTurnos1.models import medicos as mc
from django.core import serializers

from AppTurnos1.forms import medicosFormulario


def inicio (request):
    return render(request,'AppTurnos1/inicio.html')

def medicos (request):
    if request.method == "POST":
        miFormulariomedicos = medicosFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulariomedicos) 
 
        if miFormulario.is_valid:
            informacion = miFormulariomedicos.cleaned_data
            medico= medicos(nombre= informacion["nombre"], apellido= informacion["apellido"],matricula=informacion["matricula"])
            medico.save()
            return render(request, "AppTurnos1/medicos.html")

    else:
        miFormulariomedicos = medicosFormulario()
 
    return render(request, "AppTurnos1/medicos.html", {"miFormulariomedicos": miFormulariomedicos})

def medicosapi (request):
    todos_medicos=mc.objects.all()
    return HttpResponse(serializers.serialize('json', todos_medicos))    

def pacientes (request):
    return render(request,'AppTurnos1/pacientes.html')

def agendaDisponiblePorMedico (request):
    return render('AppTurnos1/agendaDisponiblePorMedico.html')

def turnoReservado (request):
    return render('AppTurnos1/turnoReservado.html')            
