from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Instrutor

@login_required(login_url='login')
def lista_instrutores(request):
    instrutores = Instrutor.objects.all()
    return render(request, 'instrutores/lista.html', {'instrutores': instrutores})