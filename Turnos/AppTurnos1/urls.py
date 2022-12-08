from django.urls import path
from AppTurnos1 import views
 
urlpatterns = [
    path('', views.inicio),
    path('medicos/', views.medico,name='medico'),
    path('medicosApi/', views.medicosapi),
    path('pacientes/', views.paciente,name='pacientes'),
    path('agendaDisponiblePorMedico/', views.agendaDisponiblePorMedico),
    path('turnoReservado/', views.turnoReservado,name='turnoReservado'),
    path('especialidad/', views.especialidad,name='especialidad'),
] 