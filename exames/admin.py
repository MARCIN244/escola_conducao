from django.contrib import admin
from .models import Exame

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'tipo', 'data', 'nota', 'resultado']
    list_filter = ['tipo', 'resultado']
    search_fields = ['aluno__usuario__first_name', 'aluno__usuario__last_name']
