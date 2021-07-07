from django import forms
from django.forms import widgets

from .models import reserva, Especialidad, Medico


class ReservaForm(forms.ModelForm):
    class Meta:
        model = reserva

        fields = [
            'rut',
            'nombre',
            'apellidos',
            'correo',
            'fecha_nacimiento',
            'sexo',
            'especialidad',
            'nombreMedico',
            'fcha',
            'hra',
            'montoR',
        ]
        labels = {
            'rut': 'rut',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'correo': 'Corre',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'sexo': 'Sexo',
            'especialidad': 'Especialidad',
            'nombreMedico': 'Nombre Medico',
            'fcha': 'Fecha reserva',
            'hra': 'Hora',
            'montoR': 'Seleccione Monto',

        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'formulario__input', 'placeholder': 'Ingresa tu rut'}),
            'nombre': forms.TextInput(attrs={'class': 'formulario__input', 'placeholder': 'Ingresa tu nombre'}),
            'apellidos':forms.TextInput(attrs={'class': 'formulario__input', 'placeholder': 'Ingresa tus apellidos'}),
            'correo': forms.EmailInput(attrs={'class': 'formulario__input', 'placeholder': 'Ingresa correo'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'formulario__input', 'placeholder': 'Ingrese su fecha nacimiento'}),
            'sexo': forms.Select(attrs={'class': 'formulario__input', 'placeholder': 'Seleccione su identidad sexual'}),
            'especialidad': forms.Select(attrs={'class': 'formulario__input', 'placeholder': 'Seleccione especialidad'}),
            'nombreMedico': forms.Select(attrs={'class': 'formulario__input', 'placeholder': 'Seleccione medico'}),
            'fcha': forms.DateInput(attrs={'class': 'formulario__input', 'placeholder': 'Ingrese fecha reserva'}),
            'hra': forms.TimeInput(attrs={'class': 'formulario__input', 'placeholder': 'Digitalice hora'}),
            'montoR': forms.TextInput(attrs={'class': 'formulario__input', 'placeholder': 'Digitalice monto'}),
        }


        
        
        