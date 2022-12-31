from django.contrib import admin
from .models import * 

admin.site.register(medicos)
admin.site.register(pacientes)
admin.site.register(especialidades)
admin.site.register(agendas)
admin.site.register(turnos)


