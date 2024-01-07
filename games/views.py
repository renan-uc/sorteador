from django.shortcuts import render
from django.http import HttpResponse
from games.forms import LotofacilForm

# Create your views here.
def sorteio(request):
    return render(request, 'sorteio.html')

def lotofacil(request):
    form = LotofacilForm()
    context = {
        'form': form
    }
    return render(request, 'lotofacil.html', context=context)


'''
import random

jogos = int(input("Número de jogos: "))
num = int(input("Número de números por jogo: "))
bilhete = []
jogo = []

for _ in range(jogos):
    for _ in range(num):
        n = random.randint(1, 25)
        while( n in jogo): # verifica se o número já está no jogo
            n = random.randint(1, 25)
        jogo.append(n)
    if jogo in bilhete: # verifica se o jogo já está no bilhete
        jogos-=1
    else:
        jogo.sort()
        bilhete.append(jogo)
    jogo = []
'''
def megasena(request):
    return render(request, 'megasena.html')

def quina(request):
    return render(request, 'quina.html')