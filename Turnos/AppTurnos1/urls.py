from django.urls import path
from AppTurnos1 import views
 
urlpatterns = [
    path('', views.inicio),
    path('medicos/', views.medicos,name='medico'),
    path('medicosApi/', views.medicosapi),
    path('pacientes/', views.pacientes,name='pacientes'),
    path('agendaDisponiblePorMedico/', views.agendaDisponiblePorMedico),
    path('turnoReservado/', views.turnoReservado,name='turnoReservado')
] 