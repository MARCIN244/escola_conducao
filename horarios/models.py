from django.db import models
from instrutores.models import Instrutor

class Horario(models.Model):
    DIA_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    instrutor = models.ForeignKey(
        Instrutor,
        on_delete=models.CASCADE,
        related_name='horarios'
    )
    dia_semana = models.CharField(max_length=10, choices=DIA_CHOICES)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.instrutor} - {self.dia_semana} {self.hora_inicio}-{self.hora_fim}"

    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'
