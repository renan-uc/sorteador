from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from django import forms

# Create your models here.
class Lotofacil(models.Model):
    qntJogos = models.IntegerField(validators=[MinValueValidator(1, message='A quantidade de jogos deve ser um número igual ou maior que 1')])
    qntNumerosPorJogo = models.IntegerField(validators=[MinValueValidator(15, message='A quantidade de números por jogo deve ser um número de 15 a 20'), MaxValueValidator(20, message='A quantidade de números por jogo deve ser um número de 15 a 20')])

    def __str__(self):
        return(f'{self.qntJogos} com {self.qntNumerosPorJogo}')
