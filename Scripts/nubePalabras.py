# -*- coding: utf-8 -*-

import pandas as pd

import limpiezaTweets as lt

import matplotlib.pyplot as plt

from wordcloud import WordCloud

import numpy as np

from PIL import Image

archivo1 = 'prueba2_sin_sentimiento.xlsx'

maskPos = np.array(Image.open('salud.jpg'))
maskNeg = np.array(Image.open('virus.jpg'))
maskNeu = np.array(Image.open('vacuna.jpg'))

df = pd.read_excel(archivo1, sheet_name='Sin sentimiento')

def colorNeg(word=None, font_size=None,position=None, orientation=None,font_path=None, random_state=None):
    h = 11 # 0 - 360
    s = 100 # 0 - 100
    l = random_state.randint(30, 70) # 0 - 100
    return "hsl({}, {}%, {}%)".format(h, s, l)

def colorPos(word=None, font_size=None,position=None, orientation=None,font_path=None, random_state=None):
    h = 125 # 0 - 360
    s = 100 # 0 - 100
    l = random_state.randint(30, 55) # 0 - 100
    return "hsl({}, {}%, {}%)".format(h, s, l)

def colorNeu(word=None, font_size=None,position=None, orientation=None,font_path=None, random_state=None):
    h = 262 # 0 - 360
    s = 36 # 0 - 100
    l = random_state.randint(30, 55) # 0 - 100
    return "hsl({}, {}%, {}%)".format(h, s, l)

#Recorre todos los tweets eliminando las palabras reservadas específicas de la nube de palabras

for i in range(len(df)):
    if type(df['tweet'].values[i])!=float:
        df['tweet'].values[i]=lt.tweetsNubePalabras(df['tweet'].values[i])
    elif type(df['tweetNuevo'].values[i])!=float and type(df['tweetCitado'].values[i])!=float:
        df['tweet'].values[i]=lt.tweetsNubePalabras(df['tweetNuevo'].values[i]+df['tweetCitado'].values[i])
    else:
        print("Error")
        

dfPositivos = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto'])
dfNegativos = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto'])
dfNeutros = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto'])
dfTotales = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto'])

#Guarda por separado los tweets positivos y negativos

for i in range(len(df)):
    if df['sentimiento'].values[i]==1:
        dfPositivos=dfPositivos.append(
            {
            'texto': df['tweet'].values[i]},
            ignore_index=True
            )
    elif df['sentimiento'].values[i]==-1:
        dfNegativos=dfNegativos.append(
            {
            'texto': df['tweet'].values[i]},
            ignore_index=True
            )
    elif df['sentimiento'].values[i]==0:
        dfNeutros=dfNeutros.append(
            {
            'texto': df['tweet'].values[i]},
            ignore_index=True
            )
    else:
        print("Error")
    dfTotales=dfTotales.append(
            {
            'texto': df['texto'].values[i]},
            ignore_index=True
            )

plt.figure(figsize = (20,20))
plt.title("Negativas").set_size(25)
plt.figure(1)
wcNeg =  WordCloud(background_color='white',mask=maskNeg,max_words = 1000 , width = 1600 , max_font_size=256,height = 800,normalize_plurals=False,
                color_func=colorNeg,collocations=False).generate(" ".join(dfNegativos['texto']))

plt.axis("off")
plt.imshow(wcNeg)

plt.figure(figsize = (20,20))
plt.title("Positivas").set_size(25)
plt.figure(2)
wcPos = WordCloud(background_color='white',mask=maskPos,max_words = 1000 , width = 1600 , max_font_size=256,height = 800,normalize_plurals=False,
                color_func=colorPos,collocations=False).generate(" ".join(dfPositivos['texto']))

plt.axis("off")
plt.imshow(wcPos)

plt.figure(figsize = (20,20))
plt.title("Neutras").set_size(25)
plt.figure(1)
wcNeu =  WordCloud(background_color='white',mask=maskNeu,max_words = 1000 , width = 1600 , max_font_size=256,height = 800,normalize_plurals=False,
                 color_func=colorNeu,collocations=False).generate(" ".join(dfNeutros['texto']))

plt.axis("off")
plt.imshow(wcNeu)

plt.figure(figsize = (20,20))
plt.title("Totales").set_size(25)
plt.figure(4)
wcTot =  WordCloud(background_color='white',mask=mask,max_words = 1000 , width = 1600 , max_font_size=256,height = 800,normalize_plurals=False,
                color_func=similar_color_func,collocations=False).generate(" ".join(dfTotales['texto']))

plt.axis("off")
plt.imshow(wcTot)
