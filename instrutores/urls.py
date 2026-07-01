from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_instrutores, name='lista_instrutores'),
]