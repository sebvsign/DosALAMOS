from django.urls import path, include
from .views import home, login_medico, recaudo, login_secretaria, vistamedico, reservaView, listado_total #,homepacientes

from . import views

urlpatterns = [
    path('', home, name="home"),
    #path('diario/', diario, name="diario"),
    #path('homepacientes/', homepacientes, name="homepacientes"),
    path('login_medico/', login_medico, name="login_medico"),
    path('login_secretaria/', login_secretaria, name="login_secretaria"),
    path('vistamedico/', vistamedico, name="vistamedico"),
    #path('paciente/', paciente, name="paciente"),
    path('recaudo/', recaudo, name="recaudo"),
    
    #path('total/', total, name="total"),
    #path('listar/', ReservaList.as_view(), name="listar"),
    #path('reserva/',ReservaCreate.as_view(), name='reserva'),
    path('reserva/', reservaView , name='reserva'),
    path('listado_total/', listado_total, name="listado_total"),
    path('accounts/', include('django.contrib.auth.urls')),
]
