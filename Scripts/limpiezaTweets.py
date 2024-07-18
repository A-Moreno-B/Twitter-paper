#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

import emoji
import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import numpy as np

"""
Funcion que devuelve una lista por palabras del texto que recibe por parámetro
"""
def tokenizador(cadena,encoding='UTF-8'):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(str(cadena).lower())

"""
Funcion que devuelve la cadena de texto recibida por parámetro después de eliminar las palabras reservadas que aparecen en ella
"""
def eliminarStopWords(cadena,encoding='UTF-8'):
    fraseFiltrada = []
    palabrasReservadas = set(stopwords.words('spanish'))
    palabrasReservadas.update([',','.',':',';','-','⊰','⊱','#','–','(',')','|','$','~','%',
                               '&','/','@','€','"','\'','“','”','..','...','>',
                               '<','[',']','¨','{','}','*','+','^','_','Ç','ª','º','`','q','d','x','v'])
    for i in cadena:
        i=borrarEmoticonos(i)
        if i[0:4]!="http" and i[0:1]!='@' and i[0:2]!="rt" and i[0:1]!='1' and i[0:1]!='2' and i[0:1]!='3' and  i[0:1]!='4' and i[0:1]!='5' and i[0:1]!='6' and i[0:1]!='7' and i[0:1]!='8' and i[0:1]!='9' and i[0:1]!='0':
            if i[0:1]=='#':
                i=i[1:]
            
            if i not in palabrasReservadas and i not in emoji.UNICODE_EMOJI['en']:
                    fraseFiltrada.append(i)
     
    return fraseFiltrada

"""
Funcion que devuelve la cadena de texto recibida por parámetro después de eliminar las palabras reservadas que aparecen en ella.
Esta función se utiliza únicamente para el gráfico de la nube de palabras
"""
def eliminarStopWordsNubePalabras(cadena,encoding='UTF-8'):
    fraseFiltrada = []
    palabrasReservadas = set(stopwords.words('spanish'))
    palabrasReservadas.update(['1','2','3','4','5','6','7','8','9','0',',','.',':',';','-','⊰','⊱','#','–','(',')','|','$','~','%','&','/','@','€','"','\'','“','”','..','...','>','<','[',']','¨','{','}','*','+','^','_','Ç','ª','º','`','q','d','x','v'])
    for i in cadena:
        i=borrarEmoticonos(i)
        if i[0:4]!="http" and i[0:1]!='@' and i[0:2]!="va" and i[0:2]!="rt" and i[0:6]!="vacuna" and i[0:5]!="covid" and i[0:2]!="si" and i[0:7]!="covid19":
            if i[0:1]=='#':
                i=i[1:]
            
            if i not in palabrasReservadas and i not in emoji.UNICODE_EMOJI['en']:
                    fraseFiltrada.append(i)
     
    return fraseFiltrada

"""
La función recibe una cadena de texto y la devuelve después de haberle quitado los emoticonos que aparecen en ella
"""
def borrarEmoticonos(string,encoding='UTF-8'):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

"""
La función recibe una cadena de texto y la devuelve después de convertir todas las palabras a su raíz
"""
def stemmizador(cadena,encoding='UTF-8'):
    stemmer = SnowballStemmer('spanish')
    stemmed = []
    for item in cadena:
        stemmed.append(stemmer.stem(item))
    return stemmed

def limpiarTweets(cadena,encoding='UTF-8'):
    contador=0
    aux=[]
    for palabra in stemmizador(eliminarStopWords(tokenizador(cadena))):
        if contador!=0:
            aux.append(" ")
            aux.append(palabra)
        else:
            aux.append(palabra)
        contador=contador+1
    return ''.join(aux)

def tweetsNubePalabras(cadena,encoding='UTF-8'):
    contador=0
    aux=[]
    for palabra in eliminarStopWordsNubePalabras(tokenizador(cadena)):
        if contador!=0:
            aux.append(" ")
            aux.append(palabra)
        else:
            aux.append(palabra)
        contador=contador+1
    return ''.join(aux)
