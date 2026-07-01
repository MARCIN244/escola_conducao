from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exame

@login_required(login_url='login')
def lista_exames(request):
    perfil = getattr(request.user, 'perfil', None)
    if perfil == 'aluno':
        exames = Exame.objects.filter(aluno__usuario=request.user)
    elif perfil == 'instrutor':
        exames = Exame.objects.filter(instrutor__usuario=request.user)
    else:
        exames = Exame.objects.all()
    return render(request, 'exames/lista.html', {'exames': exames})