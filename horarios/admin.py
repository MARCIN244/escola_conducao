from django.contrib import admin
from .models import Horario

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['instrutor', 'dia_semana', 'hora_inicio', 'hora_fim', 'disponivel']
    list_filter = ['dia_semana', 'disponivel']
    search_fields = ['instrutor__usuario__first_name', 'instrutor__usuario__last_name']