# Generated by Django 4.2.4 on 2024-01-07 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lotofacil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qntJogos', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('qntNumerosPorJogo', models.IntegerField(max_length=25, validators=[django.core.validators.MinValueValidator(15)])),
            ],
        ),
    ]
