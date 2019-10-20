from django.db import models

# Create your models here.


class Bairro(models.Model):
    nome = models.CharField('Nome', max_length=150)
    n_pessoas = models.IntegerField('Número de pessoas', null=True, blank=True)
    n_criancas_1 = models.IntegerField('Número de crianças com menos de 1 ano', null=True, blank=True)
    n_criancas = models.IntegerField('Número de Criancas', null=True, blank=True)
    n_idosos = models.IntegerField('Número de idosos', null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=150)
    uf = models.CharField('UF', max_length=3)

    @property
    def n_gravidas(self):
        return self.n_criancas_1
    
    @property
    def pop_vul(self):
        return 0.3*self.n_idoso + 0.3*self.n_criancas + 0.4*self.n_criancas_1