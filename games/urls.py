from django.urls import path
from . import views

urlpatterns = [
    path('', views.sorteio),
    path('lotofacil', views.lotofacil, name='lotofacil'),
    path('megasena', views.megasena, name='megasena'),
    path('quina', views.quina, name='quina'),
] 