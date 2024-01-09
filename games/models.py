from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
# lotofacil marca de 15 a 20 numeros dentre 25
class Lotofacil(models.Model):
    qntJogos = models.IntegerField(validators=[MinValueValidator(1, message='A quantidade de jogos deve ser um número igual ou maior que 1')])
    qntNumerosPorJogo = models.IntegerField(validators=[MinValueValidator(15, message='A quantidade de números por jogo deve ser um número de 15 a 20'), MaxValueValidator(20, message='A quantidade de números por jogo deve ser um número de 15 a 20')])

    def __str__(self):
        return(f'{self.qntJogos} com {self.qntNumerosPorJogo}')

# mega-sena marca de 6 a 20 numeros dentre 60
class MegaSena(models.Model):
    qntJogos = models.IntegerField(validators=[MinValueValidator(1, message='A quantidade de jogos deve ser um número igual ou maior que 1')])
    qntNumerosPorJogo = models.IntegerField(validators=[MinValueValidator(6, message='A quantidade de números por jogo deve ser um número de 6 a 20'), MaxValueValidator(20, message='A quantidade de números por jogo deve ser um número de 6 a 20')])

    def __str__(self):
        return(f'{self.qntJogos} com {self.qntNumerosPorJogo}')

# quina marca de 5 a 15 numeros dentre 80
class Quina(models.Model):
    qntJogos = models.IntegerField(validators=[MinValueValidator(1, message='A quantidade de jogos deve ser um número igual ou maior que 1')])
    qntNumerosPorJogo = models.IntegerField(validators=[MinValueValidator(5, message='A quantidade de números por jogo deve ser um número de 5 a 15'), MaxValueValidator(15, message='A quantidade de números por jogo deve ser um número de 5 a 15')])

    def __str__(self):
        return(f'{self.qntJogos} com {self.qntNumerosPorJogo}')