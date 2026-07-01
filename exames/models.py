from django.db import models
from alunos.models import Aluno
from instrutores.models import Instrutor

class Exame(models.Model):
    TIPO_CHOICES = [
        ('teorico', 'Teórico'),
        ('pratico', 'Prático'),
    ]

    RESULTADO_CHOICES = [
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
        ('pendente', 'Pendente'),
    ]

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='exames'
    )
    instrutor = models.ForeignKey(
        Instrutor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='exames'
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data = models.DateField()
    hora = models.TimeField()
    nota = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    nota_minima = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=10.0
    )
    resultado = models.CharField(
        max_length=10,
        choices=RESULTADO_CHOICES,
        default='pendente'
    )
    observacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.nota is not None:
            if self.nota >= self.nota_minima:
                self.resultado = 'aprovado'
            else:
                self.resultado = 'reprovado'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.aluno} - {self.tipo} - {self.data}"

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
