import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escola_conducao.settings')
django.setup()

from usuarios.models import Usuario
from alunos.models import Aluno

alunos_dados = [
    {
        'username': 'joao_silva',
        'email': 'joao@example.com',
        'password': 'senha123',
        'primeiro_nome': 'João',
        'ultimo_nome': 'Silva',
        'numero_matricula': '20240001',
    },
    {
        'username': 'maria_santos',
        'email': 'maria@example.com',
        'password': 'senha123',
        'primeiro_nome': 'Maria',
        'ultimo_nome': 'Santos',
        'numero_matricula': '20240002',
    },
    {
        'username': 'pedro_oliveira',
        'email': 'pedro@example.com',
        'password': 'senha123',
        'primeiro_nome': 'Pedro',
        'ultimo_nome': 'Oliveira',
        'numero_matricula': '20240003',
    },
]

for dados in alunos_dados:
    if Usuario.objects.filter(username=dados['username']).exists():
        print(f"⚠️ Utilizador {dados['username']} já existe")
        continue
    
    usuario = Usuario.objects.create_user(
        username=dados['username'],
        email=dados['email'],
        password=dados['password'],
        first_name=dados['primeiro_nome'],
        last_name=dados['ultimo_nome'],
    )
    usuario.perfil = 'aluno'
    usuario.save()
    
    aluno = Aluno.objects.create(
        usuario=usuario,
        numero_matricula=dados['numero_matricula']
    )
    
    print(f"✓ Aluno {dados['username']} criado com sucesso!")

print(f"\n✓ Total de alunos criados!")