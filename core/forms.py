from django import forms
from django.forms.widgets import Select, Widget

from .models import reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = reserva

        fields = ('__all__')
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'correo': 'Correo',
            'fecha_nacimiento': 'FechaNacimiento',
            'sexo': 'Sexo',
            'especialidad': 'Especialidad',
            'nombreM': 'Nombre Medico',
            'pago': 'Pago',
            'fecha_hora': 'FechaHora',
        }
        Widget = {
            'rut': forms.TextInput(attrs={'class':'formulario__input'}),
            'nombre': forms.TextInput(attrs={'class':'formulario__input'}),
            'apellidos': forms.TextInput(attrs={'class':'formulario__input'}),
            'correo': forms.TextInput(attrs={'class':'formulario__input'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'formulario__input'}),
            'sexo': forms.Select(attrs={'class':'formulario__input'}),
            'especialidad': forms.Select(attrs={'class':'formulario__input'}),
            'nombreM': forms.Select(attrs={'class':'formulario__input'}),
            'pago': forms.Select(attrs={'class':'formulario__input'}),
            'fecha_hora': forms.Select(attrs={'class':'formulario__input'}),
        }
     