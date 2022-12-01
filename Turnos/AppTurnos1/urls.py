from django.urls import path
from AppTurnos1 import views
 
urlpatterns = [
    path('medicos/', views.medicos),
    path('pacientes/', views.pacientes),
    path('agendaDisponiblePorMedico/', views.medicagendaDisponiblePorMedico),
    path('turnoReservado/', views.turnoReservado),
] 