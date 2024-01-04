from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sorteio(request):
    return render(request, 'sorteio.html')