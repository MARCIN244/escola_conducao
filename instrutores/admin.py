from django.contrib import admin
from .models import Instrutor

@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):
    list_display = ['numero_funcionario', 'get_nome', 'especialidade', 'activo']
    list_filter = ['activo']
    search_fields = ['numero_funcionario', 'usuario__first_name', 'usuario__last_name']

    def get_nome(self, obj):
        return obj.usuario.get_full_name()
    get_nome.short_description = 'Nome'