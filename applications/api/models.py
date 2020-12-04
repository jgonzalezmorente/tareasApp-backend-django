from django.db import models
from model_utils.models import TimeStampedModel


class Task(TimeStampedModel):

    STATUS_CHOICES = (
        ('0', 'Creada'),
        ('1', 'Asignada'),
        ('2', 'Cancelada'),        
        ('3', 'En proceso'),
        ('4', 'Pendiente'),
        ('5', 'En revisión'),
        ('6', 'Finalizada'),
    )

    title           = models.CharField(verbose_name='Título', max_length=100)
    description     = models.CharField(verbose_name='Descripción', max_length=200, null=True, blank=True)
    specifications  = models.TextField(verbose_name='Especificaciones', help_text='Especificaciones de la tarea', null=True, blank=True)
    estimated_hours = models.DecimalField(verbose_name='Horas estimadas', max_digits=5, decimal_places=2)
    status          = models.CharField(verbose_name='Estado', max_length=1, choices=STATUS_CHOICES)
    reason          = models.TextField(verbose_name='Motivo', help_text='Motivo del cambio de estado de la tarea', null=True, blank=True)

    class Meta:
        ordering = ['-modified']


