from django.db import models
from instrutores.models import Instrutor

class Despesa(models.Model):
    CATEGORIA_CHOICES = [
        ('combustivel', 'Combustível'),
        ('manutencao', 'Manutenção de Viaturas'),
        ('renda', 'Renda'),
        ('agua_luz', 'Água e Luz'),
        ('material', 'Material Didáctico'),
        ('outro', 'Outro'),
    ]

    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    comprovativo = models.FileField(
        upload_to='comprovativos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.categoria} - {self.valor} MZN - {self.data}"

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'


class SalarioFuncionario(models.Model):
    ESTADO_CHOICES = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
    ]

    instrutor = models.ForeignKey(
        Instrutor,
        on_delete=models.CASCADE,
        related_name='salarios'
    )
    mes = models.CharField(max_length=20)
    ano = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='pendente'
    )
    data_pagamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.instrutor} - {self.mes}/{self.ano} - {self.valor} MZN"

    class Meta:
        verbose_name = 'Salário'
        verbose_name_plural = 'Salários'
