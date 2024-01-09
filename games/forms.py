from django import forms
from games.models import Lotofacil, MegaSena, Quina

class LotofacilForm(forms.ModelForm):
    class Meta:
        model = Lotofacil
        fields = ('qntJogos', 'qntNumerosPorJogo')

class MegaSenaForm(forms.ModelForm):
    class Meta:
        model = MegaSena
        fields = ('qntJogos', 'qntNumerosPorJogo')

class QuinaForm(forms.ModelForm):
    class Meta:
        model = Quina
        fields = ('qntJogos', 'qntNumerosPorJogo')



      