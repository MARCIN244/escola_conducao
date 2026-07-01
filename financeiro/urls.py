from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_despesas, name='lista_despesas'),
]