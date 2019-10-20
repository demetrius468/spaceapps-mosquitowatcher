from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Bairro
import numpy as np
import pandas as pd
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
    qs = Bairro.objects.all().annotate(vulnerabilidade=0.3*models.F('n_idosos') + 0.3*models.F('n_criancas') + 0.4*models.F('n_criancas_1')).values()
    return JsonResponse({'res':list(qs)})
