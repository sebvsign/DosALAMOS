from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=80)
    

    def __str__(self):
        return self.especialidad 

class Medico(models.Model):
    rut = models.CharField(max_length=11)
    nombreM = models.CharField('nombre medico',max_length=80, blank=True)
    apellidos = models.CharField(max_length=80, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreM + ' ' + self.apellidos
    
class reserva(models.Model):
    SEXO_CHOICES = (
        ('0', 'Masculino'),
        ('1', 'Femenino'),
        ('2', 'OTRO'),
    )

    rut = models.CharField('rut',max_length=11)
    nombre = models.CharField('nombre',max_length=80, blank=True)
    apellidos = models.CharField('apellidos', max_length=100, blank=True)
    correo = models.EmailField('correo',max_length = 200)
    fecha_nacimiento = models.CharField('Fecha nacimiento',max_length=10, blank=True)
    sexo = models.CharField('sexo', max_length=20, choices= SEXO_CHOICES )
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE,blank=True, null=True)
    nombreMedico = models.ForeignKey(Medico, on_delete=models.CASCADE, blank=True)
    fcha = models.CharField(max_length=15, blank=True)
    hra = models.TimeField(blank=True, null=True)
    montoR = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.rut    



    





