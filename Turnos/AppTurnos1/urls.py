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
    path('especialidades/Lista/', views.especialidadList.as_view()),
] 