from django.apps import AppConfig

from .seleniumNoticias import Twitter
from keras.models import load_model
import os
import pickle

class NoticiasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'noticias'
    username = 'JavierV72565554'
    password = 'marytigrearias99'
    twitter = Twitter(username, password)

    # path = os.path.join('', "modeloRNN.h5")
    path = 'C:\\Users\\vazqu\\Desktop\\10mo\\Simulacion\\Tareas-Simulacion\\Proyecto Final\\ProyectoFinalSimulacion\\mysite\\modeloFinalRNN.h5'
    model = load_model(path)

    # path1 = os.path.join(settings.MODEL_ROOT, "tokenizerRNN.pickle")
    path1 = 'C:\\Users\\vazqu\\Desktop\\10mo\\Simulacion\\Tareas-Simulacion\\Proyecto Final\\ProyectoFinalSimulacion\\mysite\\tokenizerRNN.pickle'
    with open(path1, 'rb') as handle:
        tokenizer = pickle.load(handle)
