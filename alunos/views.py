from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Aluno
from .forms import UsuarioAlunoForm, AlunoForm

@login_required(login_url='login')
def lista_alunos(request):
    perfil = getattr(request.user, 'perfil', None)
    if perfil == 'instrutor':
        alunos = Aluno.objects.filter(instrutor__usuario=request.user)
    else:
        alunos = Aluno.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})

@login_required(login_url='login')
def adicionar_aluno(request):
    if request.method == 'POST':
        usuario_form = UsuarioAlunoForm(request.POST, request.FILES)
        aluno_form = AlunoForm(request.POST)
        if usuario_form.is_valid() and aluno_form.is_valid():
            usuario = usuario_form.save(commit=False)
            usuario.set_password(usuario_form.cleaned_data['password'])
            usuario.perfil = 'aluno'
            usuario.save()
            aluno = aluno_form.save(commit=False)
            aluno.usuario = usuario
            aluno.save()
            messages.success(request, 'Aluno adicionado com sucesso!')
            return redirect('lista_alunos')
    else:
        usuario_form = UsuarioAlunoForm()
        aluno_form = AlunoForm()
    return render(request, 'alunos/form.html', {
        'usuario_form': usuario_form,
        'aluno_form': aluno_form,
        'titulo': 'Adicionar Aluno'
    })

@login_required(login_url='login')
def detalhe_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'alunos/detalhe.html', {'aluno': aluno})

@login_required(login_url='login')
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST, instance=aluno)
        if aluno_form.is_valid():
            aluno_form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('detalhe_aluno', pk=aluno.pk)
    else:
        aluno_form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form.html', {
        'aluno_form': aluno_form,
        'aluno': aluno,
        'titulo': 'Editar Aluno'
    })
  