from django.urls import path
from AppTurnos1 import views
 
urlpatterns = [
    path('', views.inicio),
    # path('inicio', views.inicio,name='inicio'),
    path('medicos/', views.medico,name='medico'),
    path('medicosApi/', views.medicosapi),
    path('pacientes/', views.paciente,name='pacientes'),
    path('agendaDisponiblePorMedico/', views.agendaDisponiblePorMedico),
    path('turnoReservado/', views.turnoReservado,name='turnoReservado'),
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