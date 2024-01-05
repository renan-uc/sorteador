from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sorteio(request):
    return render(request, 'sorteio.html')

def lotofacil(request):
    return render(request, 'lotofacil.html')

def megasena(request):
    return render(request, 'megasena.html')

def quina(request):
    return render(request, 'quina.html')