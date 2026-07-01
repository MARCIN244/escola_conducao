from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'tipo', 'valor', 'estado', 'data_vencimento']
    list_filter = ['tipo', 'estado']
    search_fields = ['aluno__usuario__first_name', 'aluno__usuario__last_name']
