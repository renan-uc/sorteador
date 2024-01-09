from django import forms
from games.models import Lotofacil

class LotofacilForm(forms.ModelForm):
    class Meta:
        model = Lotofacil
        fields = ('qntJogos', 'qntNumerosPorJogo')

        