from django.contrib import admin
from .models import Aluno
from pagamentos.models import Pagamento
from exames.models import Exame

class PagamentoInline(admin.TabularInline):
    model = Pagamento
    extra = 0
    fields = ['tipo', 'valor', 'estado', 'data_vencimento', 'data_pagamento']

class ExameInline(admin.TabularInline):
    model = Exame
    extra = 0
    fields = ['tipo', 'data', 'nota', 'resultado']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['numero_matricula', 'get_nome', 'categoria', 'estado', 'data_matricula']
    list_filter = ['categoria', 'estado']
    search_fields = ['numero_matricula', 'usuario__first_name', 'usuario__last_name']
    inlines = [PagamentoInline, ExameInline]

    def get_nome(self, obj):
        return obj.usuario.get_full_name()
    get_nome.short_description = 'Nome'