from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=80)

    def __str__(self):
        return self.especialidad

class Medico(models.Model):
    rut = models.CharField(max_length=11)
    nombreM = models.CharField(max_length=80)
    apaterno = models.CharField(max_length=80)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombreM + ' ' +self.apaterno + ' - id especialidad: ' + str(self.especialidad)

class Pago(models.Model):
    montoR = models.FloatField()

    def __str__(self):
        return str(self.id) + ' ' + str(self.montoR)

class Hora(models.Model):
    fecha_reservaR = models.DateTimeField(null=True, blank=True)
    nombreM = models.ManyToManyField(Medico)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.fecha_reservaR) + ' - ' +str(self.nombreM)

class reserva(models.Model):
    rut = models.CharField(max_length=11)
    nombre = models.CharField(max_length=80, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    correo = models.EmailField(max_length = 200)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombreM = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name = 'nombre_medico')
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, blank=True, null=True)
    fecha_hora = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name='fecha_hora_reserva', blank=True, null=True)



