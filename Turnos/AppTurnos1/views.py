from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from AppTurnos1.models import *
from django.core import serializers 


from AppTurnos1.forms import medicosFormulario ,pacientesFormulario ,especialidadesFormulario, turnosFormularios, agendaFormularios


from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

def inicio (request):
    return render(request,"Appturnos1/index.html")

#-----------------------------------------------MEDICOS----------------------------------------#

def medicoForm (request):
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

class medicoList(ListView):
    model = medicos
    template= 'AppTurnos1/medicos_List.html'
    
class medicoCreate(CreateView):
    model = medicos
    fields= '__all__'
    success_url= '/AppTurnos1/medicos/lista/'
    
class medicoEdit(UpdateView):
    model = medicos
    fields= '__all__'
    success_url= '/AppTurnos1/medicos/lista/'
    
class medicoDetail(DetailView):
    model = medicos
    template= 'AppTurnos1/medicos_Detail.html'   
    
class medicoDelete(DeleteView):
    model = medicos     
    success_url= '/AppTurnos1/medicos/lista/'         

#-----------------------------------------------ESPECIALIDAD----------------------------------------#

def especialidadForm (request):   
    if request.method == 'POST':
        infoFormularioEspecialidad = especialidadesFormulario(request.POST) # Aqui me llega la informacion del html
        if  infoFormularioEspecialidad.is_valid():
            informacion=infoFormularioEspecialidad.cleaned_data
            especialidad=especialidades(especialidad=informacion['especialidad'])
            especialidad.save()
            return render(request,"AppTurnos1/medicos.html")
    else:
        miFormularioespecialidad= especialidadesFormulario()
    return render(request, "AppTurnos1/especialidad.html",{'miFormularioespecialidad': miFormularioespecialidad}) 
   
   
def crearespecialidad (request):   
    especialidad=especialidades(especialidad="especialidadtest")
    especialidad.save()
    return HttpResponse(f'{especialidad.especialidad}, ha sido creada')

def leerespecialidades(request):   
    especialidad_todas =especialidades.objects.all()
    contexto={"especialidad":especialidad_todas}
    print(especialidad_todas)
    #return render(request,"AppTurnos1/leerespecialidad.html", contexto)    
    return HttpResponse(serializers.serialize ('json',especialidad_todas))    
   
def editarespecialidad (request):   
    especialidad_editar ="especialidadtest"
    especialidades.objects.filter(especialidad=especialidad_editar).update(especialidad='especialidadNew')
    return HttpResponse(f'{especialidad_editar}, ha sido actualizada')
    
def borrarespecialidad (request):   
    especialidad_borrar='ttt'
    especialidad = especialidades.objects.get(especialidad=especialidad_borrar) 
    especialidad.delete()
    return HttpResponse(f'{especialidad_borrar}, ha sido eliminada')

class especialidadList(ListView):
    model = especialidades
    template= 'AppTurnos1/especialidades_List.html'
    
class especialidadCreate(CreateView):
    model = especialidades
    fields= '__all__'
    success_url= '/AppTurnos1/especialidades/lista/'#'http://127.0.0.1:8000/Appturnos1/especialidades/lista/'    

class especialidadEdit(UpdateView):
    model = especialidades
    fields= '__all__'
    success_url= '/AppTurnos1/especialidades/lista/'
    
class especialidadDetail(DetailView):
    model = especialidades
    template= 'AppTurnos1/especialidades_Detail.html'   
    
class especialidadDelete(DeleteView):
    model = especialidades       
    success_url= '/Appturnos1/especialidades/lista/'     

#-----------------------------------------------PACIENTES----------------------------------------##

def pacienteForm (request):
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

class pacienteList(ListView):
    model = pacientes
    template= 'AppTurnos1/pacientes_List.html'
        
class pacienteCreate(CreateView):
    model = pacientes
    fields= '__all__'
    success_url= '/AppTurnos1/pacientes/lista/'
    
class pacienteEdit(UpdateView):
    model = pacientes
    fields= '__all__'
    success_url= '/AppTurnos1/pacientes/lista/'
    
class pacienteDetail(DetailView):
    model = pacientes
    template= 'AppTurnos1/pacientes_Detail.html'   
    
class pacienteDelete(DeleteView):
    model = pacientes     
    success_url= '/AppTurnos1/pacientes/lista/'    
    
#-----------------------------------------------AGENDA----------------------------------------#    

def agendaForm (request):
    if request.method == "POST":
        infoFormularioAgenda= agendaFormularios(request.POST) # Aqui me llega la informacion del html
         
        if infoFormularioAgenda.is_valid():
            informacion = infoFormularioAgenda.cleaned_data
            agend= agendas(profesional=informacion["profesional"], desde=informacion["desde"],hasta=informacion["hasta"])
            agend.save()
            return render(request, "AppTurnos1/agendas.html")

    else:
        miFormularioagenda = agendaFormularios()
 
    return render(request, 'AppTurnos1/agendas.html', {"miFormularioagenda": miFormularioagenda})

class agendaList(ListView):
    model = agendas
    template= 'AppTurnos1/agendas_List.html'
        
class agendaCreate(CreateView):
    model = agendas
    fields= '__all__'
    success_url= '/AppTurnos1/agenda/lista/'
    
class agendaEdit(UpdateView):
    model = agendas
    fields= '__all__'
    success_url= '/AppTurnos1/agenda/lista/'
    
class agendaDetail(DetailView):
    model = agendas
    template= 'AppTurnos1/agenda_Detail.html'   
    
class agendaDelete(DeleteView):
    model = agendas
    success_url= '/AppTurnos1/agenda/lista/'  

#-----------------------------------------------TURNOS----------------------------------------#    
    
    
def turnoForm(request):
    if request.method == "POST":
        infoFormularioTurnos= turnosFormularios(request.POST) # Aqui me llega la informacion del html
         
        if infoFormularioTurnos.is_valid():
            informacion = infoFormularioTurnos.cleaned_data
            turno= turnos(nombre=informacion["nombre"], apellido=informacion["apellido"],  medico=informacion["medico"], Dia=informacion["Dia"]) #obraSocial=informacion["obraSocial"]
            turno.save()
            return render(request, "AppTurnos1/turnos.html")

    else:
        miFormularioturnos = turnosFormularios()
 
    return render(request, 'AppTurnos1/turnos.html', {"miFormularioturnos": miFormularioturnos})
    

class turnosList(ListView):
    model = turnos
    template= 'AppTurnos1/turnos_List.html'
        
class turnosCreate(CreateView):
    model = turnos
    fields= '__all__'
    print(fields)
    success_url= '/AppTurnos1/turnos/lista/'
    
class turnosEdit(UpdateView):
    model = turnos
    fields= '__all__'
    success_url= '/AppTurnos1/turnos/lista/'
    
class turnosDetail(DetailView):
    model = turnos
    template= 'AppTurnos1/turnos_Detail.html'   
    
class turnosDelete(DeleteView):
    model = turnos
    success_url= '/AppTurnos1/turnos/lista/'   
         