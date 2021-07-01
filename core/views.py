from django.shortcuts import render, redirect
from .models import Especialidad,Medico, reserva
from django.http import HttpResponse

from .forms import ReservaForm

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
