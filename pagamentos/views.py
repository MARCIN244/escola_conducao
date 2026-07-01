from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pagamento

@login_required(login_url='login')
def lista_pagamentos(request):
    if getattr(request.user, 'perfil', None) == 'aluno':
        pagamentos = Pagamento.objects.filter(aluno__usuario=request.user)
    else:
        pagamentos = Pagamento.objects.all()
    return render(request, 'pagamentos/lista.html', {'pagamentos': pagamentos})