from django.db import models

# Create your models here.


class Bairro(models.Model):
    nome = models.CharField('Nome', max_length=150)
    n_pessoas = models.IntegerField('Número de pessoas')
    n_criancas_1 = models.IntegerField('Número de crianças com menos de 1 ano')
    n_criancas = models.IntegerField('Número de Criancas')
    n_idosos = models.IntegerField('Número de idosos')
    cidade = models.CharField('Cidade', max_length=150)

    @property
    def n_gravidas(self):
        return self.n_criancas_1
    
    @property
    def pop_vul(self):
        return 0.3*self.n_idoso + 0.3*self.n_criancas + 0.4*self.n_criancas_1