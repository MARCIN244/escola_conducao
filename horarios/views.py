from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Despesa, SalarioFuncionario

@login_required(login_url='login')
def lista_despesas(request):
    if getattr(request.user, 'perfil', None) != 'admin':
        return render(request, 'usuarios/acesso_negado.html')
    despesas = Despesa.objects.all()
    salarios = SalarioFuncionario.objects.all()
    return render(request, 'financeiro/lista.html', {
        'despesas': despesas,
        'salarios': salarios
    })