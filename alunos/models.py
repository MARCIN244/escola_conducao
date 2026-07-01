from django.db import models
from usuarios.models import Usuario

class Aluno(models.Model):
    CATEGORIA_CHOICES = [
        ('A', 'Categoria A - Motociclos'),
        ('B', 'Categoria B - Ligeiros'),
        ('C', 'Categoria C - Pesados'),
        ('D', 'Categoria D - Transporte Colectivo'),
    ]
    
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('suspenso', 'Suspenso'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    ]

    usuario = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE,
        related_name='aluno'
    )
    numero_matricula = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    data_matricula = models.DateField(auto_now_add=True)
    instrutor = models.ForeignKey(
        'instrutores.Instrutor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alunos'
    )
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.numero_matricula}"

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'