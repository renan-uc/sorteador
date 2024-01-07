from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Lotofacil(models.Model):
    qntJogos = models.IntegerField(validators=[MinValueValidator(1)])
    qntNumerosPorJogo = models.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(25)])