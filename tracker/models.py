from django.db import models

# Create your models here.


class Bairro(models.Model):
    n_pessoas = models.IntegerField('Número de pessoas')
    n_criancas_1 = models.IntegerField('Número de crianças com menos de 1 ano')
    n_idosos = models.IntegerField('Número de idosos')
    
    @property
    def n_gravidas(self):
        return n_criancas_1