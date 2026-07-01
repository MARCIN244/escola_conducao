from django.db import models
from alunos.models import Aluno

class Pagamento(models.Model):
    ESTADO_CHOICES = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
        ('atrasado', 'Atrasado'),
    ]

    TIPO_CHOICES = [
        ('matricula', 'Matrícula'),
        ('propina', 'Propina'),
        ('exame', 'Exame'),
        ('outro', 'Outro'),
    ]

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='pagamentos'
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='pendente'
    )
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    recibo_numero = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.aluno} - {self.tipo} - {self.valor} MZN"

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'