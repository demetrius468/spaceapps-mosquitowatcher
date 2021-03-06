# Generated by Django 2.2.3 on 2019-10-20 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('n_pessoas', models.IntegerField(verbose_name='Número de pessoas')),
                ('n_criancas_1', models.IntegerField(verbose_name='Número de crianças com menos de 1 ano')),
                ('n_idosos', models.IntegerField(verbose_name='Número de idosos')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
            ],
        ),
    ]
