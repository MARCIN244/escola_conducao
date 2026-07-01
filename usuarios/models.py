from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    PERFIL_CHOICES = [
        ('admin', 'Administrador'),
        ('instrutor', 'Instrutor'),
        ('aluno', 'Aluno'),
    ]
    
    perfil = models.CharField(
        max_length=20, 
        choices=PERFIL_CHOICES, 
        default='aluno'
    )
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(
        upload_to='fotos/', 
        blank=True, 
        null=True
    )
    bilhete_identidade = models.CharField(max_length=20, blank=True, unique=True, null=True)
    endereco = models.CharField(max_length=255, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='+'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='+'
    )

    def __str__(self):
        return f"{self.get_full_name()} ({self.perfil})"

    def is_admin(self):
        return self.perfil == 'admin'

    def is_instrutor(self):
        return self.perfil == 'instrutor'

    def is_aluno(self):
        return self.perfil == 'aluno'