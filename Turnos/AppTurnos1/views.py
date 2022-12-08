from django.shortcuts import render
from django.http import HttpResponse

from AppTurnos1.models import medicos, pacientes, Especialidades 
from django.core import serializers

from AppTurnos1.forms import medicosFormulario ,pacientesFormulario ,especialidadesFormulario


def inicio (request):
    return render(request,"Appturnos1/index.html")

def medico (request):
    if request.method == "POST":
        infoFormulariomedicos = medicosFormulario(request.POST) # Aqui me llega la informacion del html
         
        if infoFormulariomedicos.is_valid():
            informacion = infoFormulariomedicos.cleaned_data
            medico= medicos(nombre=informacion["nombre"], apellido=informacion["apellido"],matricula=informacion["matricula"])
            medico.save()
            return render(request, "AppTurnos1/medicos.html")

    else:
        miFormulariomedicos = medicosFormulario()
 
    return render(request, "AppTurnos1/medicos.html", {"miFormulariomedicos": miFormulariomedicos})

def medicosapi (request):
    todos_medicos=medicos.objects.all()
    return HttpResponse(serializers.serialize('json', todos_medicos))    

def especialidadForm (request):   
    if request.method == 'POST':
        infoFormularioEspecialidad = especialidadesFormulario(request.POST) # Aqui me llega la informacion del html
        if  infoFormularioEspecialidad.is_valid():
            informacion=infoFormularioEspecialidad.cleaned_data
            especialidad=Especialidades(especialidad=informacion['especialidad'])
            especialidad.save()
            return render(request,"AppTurnos1/medicos.html")
    else:
        miFormularioespecialidad= especialidadesFormulario()
    return render(request, "AppTurnos1/especialidad.html",{'miFormularioespecialidad': miFormularioespecialidad}) 
   
   
   
   # if miFormularioEspecialidad.is_valid():
   #         informacion = miFormularioEspecialidad.cleaned_data
   #         especialidad = informacion['especialidad']
   #         especialidad= Especialidades(especialidad= especialidad)
   #         especialidad.save()
   #         return render(request, "AppTurnos1/especialdad.html",{"miFormularioEspecialidad":miFormularioEspecialidad}) 

def paciente (request):
    if request.method == "POST":
        infoFormularioPacientes = pacientesFormulario(request.POST) # Aqui me llega la informacion del html
         
        if infoFormularioPacientes.is_valid():
            informacion = infoFormularioPacientes.cleaned_data
            paciente= pacientes(nombre=informacion["nombre"], apellido=informacion["apellido"], obraSocial=informacion["obraSocial"], fechaNacimento=informacion["fechaNacimento"])
            paciente.save()
            return render(request, "AppTurnos1/pacientes.html")

    else:
        miFormulariopacientes = pacientesFormulario()
 
    return render(request, "AppTurnos1/pacientes.html", {"miFormulariopacientes": miFormulariopacientes})

def agendaDisponiblePorMedico (request):
    return render('AppTurnos1/agendaDisponiblePorMedico.html')

def turnoReservado (request):
    return render('AppTurnos1/turnoReservado.html')            
