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
            'nombre': forms.TextInput(attrs={'class': 'formulario__input'}),
            'apellidos':forms.TextInput(attrs={'class': 'formulario__input'}),
            'correo': forms.EmailInput(attrs={'class': 'formulario__input'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'formulario__input'}),
            'sexo': forms.Select(attrs={'class': 'formulario__input'}),
            'especialidad': forms.Select(attrs={'class': 'formulario__input'}),
            'nombreMedico': forms.Select(attrs={'class': 'formulario__input'}),
            'fcha': forms.DateInput(attrs={'class': 'formulario__input'}),
            'hra': forms.TimeInput(attrs={'class': 'formulario__input'}),
            'montoR': forms.TextInput(attrs={'class': 'formulario__input'}),
        }


        
        
        