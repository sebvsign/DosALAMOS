from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def diario(request):
    return render(request, 'core/diario.html')

def homepacientes(request):
    return render(request, 'core/homepacientes.html')

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
