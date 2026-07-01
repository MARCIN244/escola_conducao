from django.db import models
from usuarios.models import Usuario

class Instrutor(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='instrutor'
    )
    numero_funcionario = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100, blank=True)
    data_contratacao = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.numero_funcionario}"

    class Meta:
        verbose_name = 'Instrutor'
        verbose_name_plural = 'Instrutores'
