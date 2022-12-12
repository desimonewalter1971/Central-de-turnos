from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from AppTurnos1.models import medicos, pacientes, especialidades 
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

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class especialidadList(ListView):
    model = especialidades
    template= 'Appturnos1/especialidades_List.html'
    
class especialidadCreate(CreateView):
    model = especialidades
    fields= '__all__'
    success_url= '/Appturnos1/especialidades/lista/'#'http://127.0.0.1:8000/Appturnos1/especialidades/lista/'    

class especialidadEdit(UpdateView):
    model = especialidades
    fields= '__all__'
    success_url= '/Appturnos1/especialidades/lista/'
    
class especialidadDetail(DetailView):
    model = especialidades
    template= 'Appturnos1/especialidades_Detail.html'   
    
class especialidadDelete(DeleteView):
    model = especialidades       
    success_url= '/Appturnos1/especialidades/lista/'     

#

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

# MEDICOS

class medicoList(ListView):
    model = medicos
    template= 'Appturnos1/medicos_List.html'
    
class medicoCreate(CreateView):
    model = medicos
    fields= '__all__'
    success_url= '/Appturnos1/medicos/lista/'
    
class medicoEdit(UpdateView):
    model = medicos
    fields= '__all__'
    success_url= '/Appturnos1/medicos/lista/'
    
class medicoDetail(DetailView):
    model = medicos
    template= 'Appturnos1/medicos_Detail.html'   
    
class medicoDelete(DeleteView):
    model = medicos     
    success_url= '/Appturnos1/medicos/lista/'         

# PACIENTES

class pacienteList(ListView):
    model = pacientes
    template= 'Appturnos1/pacientes_List.html'
        
class pacienteCreate(CreateView):
    model = pacientes
    fields= '__all__'
    success_url= '/Appturnos1/pacientes/lista/'
    
class pacienteEdit(UpdateView):
    model = pacientes
    fields= '__all__'
    success_url= '/Appturnos1/pacientes/lista/'
    
class pacienteDetail(DetailView):
    model = pacientes
    template= 'Appturnos1/pacientes_Detail.html'   
    
class pacienteDelete(DeleteView):
    model = pacientes     
    success_url= '/Appturnos1/pacientes/lista/'    