from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_exames, name='lista_exames'),
]