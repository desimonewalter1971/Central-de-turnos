from django.urls import path
from AppTurnos1 import views
 
urlpatterns = [
    path('', views.inicio),
    # path('inicio', views.inicio,name='inicio'),
    path('medicos/', views.medico,name='medico'),    
    path('medicos/lista/', views.medicoList.as_view(),name='Listmedico'),
    path('medicos/crear/', views.medicoCreate.as_view(),name='Newmedico'),
    path('medicos/editar/<pk>', views.medicoEdit.as_view(),name='Editmedico'),
    path('medicos/detalle/<pk>', views.medicoDetail.as_view(),name='Detailmedico'),
    path('medicos/borrar/<pk>', views.medicoDelete.as_view(),name='Deletemedico'),
    path('medicosApi/', views.medicosapi),
    #
    path('agendaDisponiblePorMedico/', views.agendaDisponiblePorMedico),
    path('turnoReservado/', views.turnoReservado,name='turnoReservado'),
    #
    path('pacientes/', views.paciente,name='pacientes'),
    path('pacientes/lista/', views.pacienteList.as_view(),name='Listpaciente'),
    path('pacientes/crear/', views.pacienteCreate.as_view(),name='Newpaciente'),
    path('pacientes/editar/<pk>', views.pacienteEdit.as_view(),name='Editpaciente'),
    path('pacientes/detalle/<pk>', views.pacienteDetail.as_view(),name='Detailpaciente'),
    path('pacientes/borrar/<pk>', views.pacienteDelete.as_view(),name='Deletepaciente'),
    #
    path('especialidad/', views.especialidadForm,name='especialidad'),
    path('crearespecialidad/', views.crearespecialidad),
    path('leerespecialidades/', views.leerespecialidades),
    path('editarespecialidad/', views.editarespecialidad),
    path('borrarespecialidad/', views.borrarespecialidad),
    path('especialidades/lista/', views.especialidadList.as_view(),name='List'),
    path('especialidades/crear/', views.especialidadCreate.as_view(),name='New'),
    path('especialidades/editar/<pk>', views.especialidadEdit.as_view(),name='Edit'),
    path('especialidades/detalle/<pk>', views.especialidadDetail.as_view(),name='Detail'),
    path('especialidades/borrar/<pk>', views.especialidadDelete.as_view(),name='Delete'),
] 