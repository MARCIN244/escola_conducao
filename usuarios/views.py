from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Utilizador ou palavra-passe incorrectos!')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    hoje = timezone.now().date()
    context = {}
    perfil = getattr(request.user, 'perfil', 'admin')

    if perfil == 'admin' or request.user.is_superuser:
        from alunos.models import Aluno
        from instrutores.models import Instrutor
        from aulas.models import Aula
        from pagamentos.models import Pagamento
        context = {
            'total_alunos': Aluno.objects.count(),
            'total_instrutores': Instrutor.objects.count(),
            'aulas_hoje': Aula.objects.filter(data=hoje).count(),
            'pagamentos_pendentes': Pagamento.objects.filter(estado='pendente').count(),
        }
    elif perfil == 'instrutor':
        from aulas.models import Aula
        from exames.models import Exame
        from alunos.models import Aluno
        context = {
            'total_alunos': Aluno.objects.filter(instrutor__usuario=request.user).count(),
            'aulas_hoje': Aula.objects.filter(instrutor__usuario=request.user, data=hoje).count(),
            'exames_mes': Exame.objects.filter(instrutor__usuario=request.user, data__month=hoje.month).count(),
        }
    elif perfil == 'aluno':
        from aulas.models import Aula
        from exames.models import Exame
        from pagamentos.models import Pagamento
        context = {
            'total_aulas': Aula.objects.filter(aluno__usuario=request.user).count(),
            'total_exames': Exame.objects.filter(aluno__usuario=request.user).count(),
            'pagamentos_pendentes': Pagamento.objects.filter(aluno__usuario=request.user, estado='pendente').count(),
        }

    return render(request, 'usuarios/dashboard.html', context)