# Generated by Django 4.2.4 on 2024-01-09 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_megasena'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qntJogos', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='A quantidade de jogos deve ser um número igual ou maior que 1')])),
                ('qntNumerosPorJogo', models.IntegerField(validators=[django.core.validators.MinValueValidator(5, message='A quantidade de números por jogo deve ser um número de 5 a 15'), django.core.validators.MaxValueValidator(15, message='A quantidade de números por jogo deve ser um número de 5 a 15')])),
            ],
        ),
    ]