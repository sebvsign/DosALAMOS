from core.admin import ReservaAdmin
from django.shortcuts import render, redirect
from .models import Especialidad,Medico, reserva
from django.http import HttpResponse
from django.db.models import Sum
from django.db.models import Avg, Max, Min, Count



from .forms import ReservaForm
from core.models import reserva


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def diario(request):
    return render(request, 'core/diario.html')

def reservaView(request):
    data = {
        'form': ReservaForm()
    }

    if request.method == 'POST':
        formulario = ReservaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado"
        else:
            data["form"] = formulario
            
    return render(request, 'core/reserva.html', data)

def login_medico(request):
    return render(request, 'core/login_medico.html')

def login_secretaria(request):
    return render(request, 'core/login_secretaria.html')

def vistamedico(request):
    return render(request, 'core/vistamedico.html')

def paciente(request):
    return render(request, 'core/paciente.html')

def recaudo(request):
    return render(request, 'core/recaudo.html')

def total(request):
    return render(request, 'core/total.html')

def listado_total(request):
        Reserva = reserva.objects.all()
        data = {
            'Reserva':Reserva,
            
        }
        return render(request, 'core/listado_total.html', data)

   