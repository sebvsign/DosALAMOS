from django.contrib import admin
from .models import Especialidad, Medico, reserva, Hora, Pago
# Register your models here.



admin.site.register(reserva)

#######################################

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'especialidad'
    )   

admin.site.register(Especialidad, EspecialidadAdmin)

#######################################

class HoraAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'fecha_reservaR',
    )

admin.site.register(Hora, HoraAdmin)

#######################################

class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rut',
        'nombreM',
        'apaterno',
        'especialidad'
    )   

admin.site.register(Medico, MedicoAdmin)

#######################################

class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'montoR',
    )   


admin.site.register(Pago, MedicoAdmin)