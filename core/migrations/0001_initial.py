# Generated by Django 2.1.15 on 2021-07-03 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=11)),
                ('nombreM', models.CharField(blank=True, max_length=80, verbose_name='nombre medico')),
                ('apellidos', models.CharField(blank=True, max_length=80)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=11, verbose_name='rut')),
                ('nombre', models.CharField(blank=True, max_length=80, verbose_name='nombre')),
                ('apellidos', models.CharField(blank=True, max_length=100, verbose_name='apellidos')),
                ('correo', models.EmailField(max_length=200, verbose_name='correo')),
                ('fecha_nacimiento', models.CharField(blank=True, max_length=10, verbose_name='Fecha nacimiento')),
                ('sexo', models.CharField(choices=[('0', 'Masculino'), ('1', 'Femenino'), ('2', 'OTRO')], max_length=20, verbose_name='sexo')),
                ('fechaR', models.CharField(blank=True, max_length=15, verbose_name='Fecha')),
                ('horaR', models.TimeField(blank=True, null=True, verbose_name='Hora')),
                ('montoR', models.FloatField(blank=True, choices=[('0', 0), ('1', 5000)], null=True)),
                ('especialidad', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Especialidad')),
                ('nombreMedico', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Medico')),
            ],
        ),
    ]
