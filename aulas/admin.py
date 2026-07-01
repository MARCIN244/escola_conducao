from django.contrib import admin
from .models import Aula

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'instrutor', 'tipo', 'data', 'hora_inicio', 'estado']
    list_filter = ['tipo', 'estado']
    search_fields = ['aluno__usuario__first_name', 'aluno__usuario__last_name']