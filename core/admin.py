from django.contrib import admin
from .models import Especialidad, Medico, reserva
# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
   search_fields =['rut'] 
   list_per_page = 10

#class ReservaAdmin(admin.ModelAdmin):
#    list_display = (
#        'rut',
#        'fullname',
#        'correo',
#        'fecha_nacimiento',
#        'sexo',
#        'hora',
#        'Nombre_Medico',
#        'Especialidad',
#        'Monto'
#    )
#    def fullname(self, obj):
#        return obj.nombre + ' ' + obj.apellidos
#    def hora (self, obj):
#        return obj.Hora.fecha+' ' +str(obj.Hora.hora)
#    def Nombre_Medico(self, obj):
#        return obj.Hora.nombreM.nombreM + ' ' + obj.Hora.nombreM.apellidos
    
#    def Especialidad(self, obj):
#        return obj.Hora.nombreM.especialidad.especialidad
    
#    def Monto(self, obj):
#        return obj.Hora.nombreM.especialidad.montoR


admin.site.register(reserva)#, ReservaAdmin)

#-------------------------------------------------

admin.site.register(Especialidad)
admin.site.register(Medico)

