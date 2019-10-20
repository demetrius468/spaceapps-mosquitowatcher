from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Bairro
import numpy as np
import pandas as pd
from django.db import models
# Create your views here.

def bairros(request, cidade):
    qs = Bairro.objects.filter(cidade=cidade).values_list('nome')
    return JsonResponse({'data': list(qs)})


def weight(request):
    lat = request.GET['lat']
    long = request.GET['long']
    cidade = request.GET['cidade']
    df_lat = pd.read_csv('tracker/Latitude.csv', dtype=np.float, delimiter=';', header=None)
    df_long = pd.read_csv('tracker/Longitude.csv', dtype=np.float, delimiter=';',header=None)
    res = np.sqrt(((df_lat - float(lat))**2) + ((df_long - float(long))**2))
    x, y = np.unravel_index(res.values.argmin(), res.shape)
    df_temp = pd.read_csv('tracker/SurfSkinTemp_Forecast_A.csv', dtype=np.float, delimiter=';', header=None)
    df_precip = pd.read_csv('tracker/IR_Precip_Est_A.csv', dtype=np.float, delimiter=';', header=None)
    temp = df_temp.iloc[x, y]
    precip = df_precip.iloc[x, y]
    qs = Bairro.objects.filter(cidade__icontains=cidade).annotate(vulnerabilidade=0.3*models.F('n_idosos') + 0.3*models.F('n_criancas') + 0.4*models.F('n_criancas_1')).values()
    return JsonResponse({'res':list(qs)})

def gerar_df():
    df = pd.read_excel('tracker/censo/sinopse_AC.xls')
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_AL.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_AM.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_AP.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_BA.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_CE.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_DF.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_ES.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_GO.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_MA.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_MG.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_MS.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_MT.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_PA.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_PB.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_PE.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_PI.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_PR.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_RJ.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_RN.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_RO.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_RR.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_RS.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_SC.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_SE.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_SP_RM_SP_Santos.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_SP_RM.xls')])
    df = pd.concat([df, pd.read_excel('tracker/censo/sinopse_TO.xls')])
    return df

def adicionar_bairros():
    #df = gerar_df()
    #df.to_csv('bairros.csv')
    #df = pd.read_csv('bairros.csv')
    #df = df.replace('X', 0)
    #df.index = np.arange(df.shape[0]) 
    df = pd.read_excel('tracker/censo/sinopse_SE.xls')
    df = df.replace('X', 0)
    for i in range(df.shape[0]):
        uf = df.loc[i, 'Nome_da_UF ']
        cidade = df.loc[i, 'Nome_do_municipio']
        bairro_nome= df.loc[i, 'Nome_do_bairro']
        n_pessoas = int(df.loc[i, 'V014'])
        n_criancas_1 = int(df.loc[i, 'V032']) + int(df.loc[i, 'V033'])
        n_criancas = int(df.loc[i, 'V032']) + int(df.loc[i, 'V033']) + int(df.loc[i, 'V034']) + int(df.loc[i, 'V035']) + int(df.loc[i, 'V036']) + int(df.loc[i, 'V037']) + int(df.loc[i, 'V038']) + int(df.loc[i, 'V039']) + int(df.loc[i, 'V040']) + int(df.loc[i, 'V041']) + int(df.loc[i, 'V042']) + int(df.loc[i, 'V043']) +  int(df.loc[i, 'V044'])
        n_idosos = int(df.loc[i, 'V064']) + int(df.loc[i, 'V065']) + int(df.loc[i, 'V066']) + int(df.loc[i, 'V067']) + int(df.loc[i, 'V068']) + int(df.loc[i, 'V069']) + int(df.loc[i, 'V070']) + int(df.loc[i, 'V071']) + int(df.loc[i, 'V072']) + int(df.loc[i, 'V073']) + int(df.loc[i, 'V074']) + int(df.loc[i, 'V075']) + int(df.loc[i, 'V076']) +  int(df.loc[i, 'V077'])
        bairro, c = Bairro.objects.get_or_create(nome=bairro_nome, cidade=cidade, uf=uf)
        if c:
            bairro.n_pessoas = n_pessoas
            bairro.n_criancas_1 = n_criancas_1
            bairro.n_criancas = n_criancas
            bairro.n_idosos = n_idosos
        else:
            bairro.n_pessoas += n_pessoas
            bairro.n_criancas_1 += n_criancas_1
            bairro.n_criancas += n_criancas
            bairro.n_idosos += n_idosos
        bairro.save()
        print('Faltam', df.shape[0] - i, 'registros')
