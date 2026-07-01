from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Despesa, SalarioFuncionario

@login_required(login_url='login')
def lista_despesas(request):
    perfil = getattr(request.user, 'perfil', None)
    if perfil != 'admin' and not request.user.is_superuser:
        return render(request, 'usuarios/acesso_negado.html')
    despesas = Despesa.objects.all()
    salarios = SalarioFuncionario.objects.all()
    return render(request, 'financeiro/lista.html', {
        'despesas': despesas,
        'salarios': salarios
    })