import os
import pathlib
import pandas as pd
import numpy as np
import pandas as pd
from string import punctuation
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical

from keras.models import model_from_json
from keras.models import load_model
from pandas import DataFrame

import nltk
from nltk.stem.wordnet import WordNetLemmatizer

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from string import punctuation

import sqlite3
import pickle

from tensorflow.python.keras.models import Sequential

from noticias.apps import NoticiasConfig

class modeloRNN:

    def request(self,userText):
        twt = [userText]

        print('Tweet',twt)
        
        twt = NoticiasConfig.tokenizer.texts_to_sequences(twt)
        
        num_Columnas=NoticiasConfig.model.input_shape[1]
        twt = pad_sequences(twt, maxlen=num_Columnas, dtype='int32', value=0)
        respuesta = self.predict(twt)
        return respuesta
    

    def predict(self,twt):
        try:
            sentiment = NoticiasConfig.model.predict(twt,batch_size=1,verbose = 2)[0]
            print(sentiment)
            print(np.argmax(sentiment))
            respuesta=""
            if(np.argmax(sentiment) == 0):
                prob = sentiment[0]
                respuesta = ("%s %.2f%%" % ('Noticia falsa con certeza del', prob*100))
                print(respuesta)
                return [0,respuesta]
            elif (np.argmax(sentiment) == 1):
                prob = sentiment[1]
                respuesta = ("%s %.2f%%" % ('Noticia verdadera con certeza del', prob*100))
                print(respuesta)
                return [1, respuesta]
            
            return respuesta
        except KeyError:
            respuesta='No comprendo tu comentario'
            print(respuesta)
            return respuesta