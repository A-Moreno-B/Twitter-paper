# -*- coding: utf-8 -*-

import pandas as pd

import limpiezaTweets as lt

archivo1 = 'prueba2_neutros.xlsx'

df = pd.read_excel(archivo1, sheet_name='Neutros')

dfAux = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])

#Limpia los tweets y junta los tweets que tengan los campos tweetNuevo y tweetCitado en un mismo campo

for i in range(len(df)):
    if type(df['tweet'].values[i])!=float:
        df['tweet'].values[i]=lt.limpiarTweets(df['tweet'].values[i])
    elif type(df['tweetNuevo'].values[i])!=float and type(df['tweetCitado'].values[i])!=float:
        df['tweet'].values[i]=lt.limpiarTweets(df['tweetNuevo'].values[i]+df['tweetCitado'].values[i])
    else:
        print("Error")
        
    
for i in range(len(df)):
        dfAux=dfAux.append(
              {'NumeroRetweets': df['NumeroRetweets'].values[i],
              'timestamp': df['timestamp'].values[i],
              'texto': lt.limpiarTweets(df['tweet'].values[i]),
              'sentimiento': df['sentimiento'].values[i]},
              ignore_index=True
              )

dfAux.to_excel("prueba2Neutros.xlsx")