from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
from django.http import JsonResponse
from .apps import NoticiasConfig
from .scripts.rnn import modeloRNN

# Create your views here.

class ApiNoticias (APIView):
    def __init__(self):
        self.object = modeloRNN()

    def get(self, request):
        #Obtener del GET
        link = request.GET.get('link')
        tweet = NoticiasConfig.twitter.obtenerContenidoUrl(link)

        respuesta = self.object.request(tweet)
        print("El texto de entrada ", tweet)

        return JsonResponse({'id': respuesta[0],'respuesta': respuesta[1]})

class ApiNoticiasTexto(APIView):
    def __init__(self):
        self.object = modeloRNN()

    def get(self, request):
        #Obtener del GET
        texto = request.GET.get('texto')
        print("El texto de entrada ", texto)
        respuesta = self.object.request(texto)
        print(respuesta)
        return JsonResponse({'id': respuesta[0],'respuesta': respuesta[1]})