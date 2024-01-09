import random
from django.shortcuts import render
from django.http import HttpResponse
from games.forms import LotofacilForm
from games.models import Lotofacil

def sorteador(qntJogos, qntNumerosPorJogo):
    bilhete = []
    jogo = []

    for _ in range(qntJogos):
        for _ in range(qntNumerosPorJogo):
            n = random.randint(1, 25)
            while( n in jogo): # verifica se o número já está no jogo
                n = random.randint(1, 25)
            jogo.append(n)
        if jogo in bilhete: # verifica se o jogo já está no bilhete
            qntJogos-=1
        else:
            jogo.sort()
            bilhete.append(jogo)
        jogo = []
    
    return bilhete

# Create your views here.
def sorteio(request):
    return render(request, 'sorteio.html')

def lotofacil(request):
    if request.method == "GET":
        form = LotofacilForm()
        return render(request, 'lotofacil.html', {'form':form})

    elif request.method == "POST":
        form = LotofacilForm(request.POST)
        if form.is_valid():
            lotofacil = form.save(commit=False) 
            jogos = lotofacil.qntJogos
            num = lotofacil.qntNumerosPorJogo
            bilhete = sorteador(jogos, num)
            lotofacil.save()
            return render(request, 'lotofacil.html', {'form':form, 'bilhete':bilhete})
        else:
            return render(request, 'lotofacil.html', {'form':form})
            
def megasena(request):
    return render(request, 'megasena.html')

def quina(request):
    return render(request, 'quina.html')