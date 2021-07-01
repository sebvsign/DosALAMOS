from django import forms

from .models import reserva

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
            'Hora',
        ]
        widgets = {
            'hora': forms.Select(attrs={'Class':'formulario__input'}),
        }
        def Hora(self, obj):
            return obj.Hora.hora
        
        
        