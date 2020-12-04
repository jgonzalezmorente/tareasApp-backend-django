from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel

User = get_user_model()

class UserRole(TimeStampedModel):

    ROLE_CHOICES = (
        ('MANAGER', 'Responsable'),
        ('EMPLOYEE', 'Empleado')
    )

    role  = models.CharField(verbose_name='Rol', max_length=10, choices=ROLE_CHOICES)
    users = models.ManyToManyField(User, verbose_name='Usuarios', related_name='get_role')

    class Meta:
        verbose_name        = 'Asignación de rol'
        verbose_name_plural = 'Asignación de roles'
        ordering            = ['role']
    
    def __str__(self):
        return self.role

