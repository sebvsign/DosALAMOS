# Generated by Django 2.1.15 on 2021-07-03 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='fechaR',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='horaR',
        ),
        migrations.AddField(
            model_name='reserva',
            name='fcha',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hra',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
