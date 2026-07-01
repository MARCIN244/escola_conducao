from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    path('<int:pk>/', views.detalhe_aluno, name='detalhe_aluno'),
    path('<int:pk>/editar/', views.editar_aluno, name='editar_aluno'),
]