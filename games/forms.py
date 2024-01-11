from django import forms
from games.models import Lotofacil, MegaSena, Quina

class LotofacilForm(forms.ModelForm):
    class Meta:
        model = Lotofacil
        fields = ('qntJogos', 'qntNumerosPorJogo')
        labels = {
            'qntJogos': 'QUANTIDADE DE JOGOS',
            'qntNumerosPorJogo' : 'QUANTIDADE DE NÚMEROS POR JOGO',
        }

class MegaSenaForm(forms.ModelForm):
    class Meta:
        model = MegaSena
        fields = ('qntJogos', 'qntNumerosPorJogo')
        labels = {
            'qntJogos': 'QUANTIDADE DE JOGOS',
            'qntNumerosPorJogo' : 'QUANTIDADE DE NÚMEROS POR JOGO',
        }


class QuinaForm(forms.ModelForm):
    class Meta:
        model = Quina
        fields = ('qntJogos', 'qntNumerosPorJogo')
        labels = {
            'qntJogos': 'QUANTIDADE DE JOGOS',
            'qntNumerosPorJogo' : 'QUANTIDADE DE NÚMEROS POR JOGO',
        }




      