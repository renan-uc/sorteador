from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Lotofacil(models.Model):
    qntJogos = models.IntegerField()
    qntNumerosPorJogo = models.IntegerField()

    def __str__(self):
        return(f'{self.qntJogos} com {self.qntNumerosPorJogo}')