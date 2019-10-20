from django.urls import path
from .views import *
urlpatterns = [
    path('bairros/<str:cidade>', bairros, name='bairros'),
    path('bairros/', weight, name='weight')
]