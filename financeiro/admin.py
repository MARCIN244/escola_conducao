from django.contrib import admin
from .models import Despesa, SalarioFuncionario

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'descricao', 'valor', 'data']
    list_filter = ['categoria']

@admin.register(SalarioFuncionario)
class SalarioAdmin(admin.ModelAdmin):
    list_display = ['instrutor', 'mes', 'ano', 'valor', 'estado']
    list_filter = ['estado', 'ano']