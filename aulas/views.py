from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Aula

@login_required(login_url='login')
def lista_aulas(request):
    perfil = getattr(request.user, 'perfil', None)
    if perfil == 'aluno':
        aulas = Aula.objects.filter(aluno__usuario=request.user)
    elif perfil == 'instrutor':
        aulas = Aula.objects.filter(instrutor__usuario=request.user)
    else:
        aulas = Aula.objects.all()
    return render(request, 'aulas/lista.html', {'aulas': aulas})