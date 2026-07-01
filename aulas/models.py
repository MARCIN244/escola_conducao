from django.db import models
from alunos.models import Aluno
from instrutores.models import Instrutor

class Aula(models.Model):
    ESTADO_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    TIPO_CHOICES = [
        ('teorica', 'Teórica'),
        ('pratica', 'Prática'),
    ]

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aulas'
    )
    instrutor = models.ForeignKey(
        Instrutor,
        on_delete=models.CASCADE,
        related_name='aulas'
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='agendada'
    )
    observacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.tipo} - {self.data}"

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
