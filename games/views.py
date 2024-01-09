import random
from django.shortcuts import render
from django.http import HttpResponse
from games.forms import LotofacilForm, MegaSenaForm, QuinaForm
from games.models import Lotofacil, MegaSena, Quina

def sorteador(qntJogos, qntNumerosPorJogo, numDisponiveis):
    bilhete = []
    jogo = []

    for _ in range(qntJogos):
        for _ in range(qntNumerosPorJogo):
            n = random.randint(1, numDisponiveis)
            while( n in jogo): # verifica se o número já está no jogo
                n = random.randint(1, numDisponiveis)
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
            bilhete = sorteador(jogos, num, 25)
            lotofacil.save()
            return render(request, 'lotofacil.html', {'form':form, 'bilhete':bilhete})
        else:
            return render(request, 'lotofacil.html', {'form':form})
            
def megasena(request):
    if request.method == "GET":
        form = MegaSenaForm()
        return render(request, 'megasena.html', {'form':form})

    elif request.method == "POST":
        form = MegaSenaForm(request.POST)
        if form.is_valid():
            megasena = form.save(commit=False) 
            jogos = megasena.qntJogos
            num = megasena.qntNumerosPorJogo
            bilhete = sorteador(jogos, num, 60)
            megasena.save()
            return render(request, 'megasena.html', {'form':form, 'bilhete':bilhete})
        else:
            return render(request, 'megasena.html', {'form':form})

def quina(request):
    if request.method == "GET":
        form = QuinaForm()
        return render(request, 'quina.html', {'form':form})

    elif request.method == "POST":
        form = QuinaForm(request.POST)
        if form.is_valid():
            quina = form.save(commit=False) 
            jogos = quina.qntJogos
            num = quina.qntNumerosPorJogo
            bilhete = sorteador(jogos, num, 80)
            quina.save()
            return render(request, 'quina.html', {'form':form, 'bilhete':bilhete})
        else:
            return render(request, 'quina.html', {'form':form})
