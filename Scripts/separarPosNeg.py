# -*- coding: utf-8 -*-

import pandas as pd

import limpiezaTweets as lt

archivo1 = 'losQueHayQueAnalizar.xlsx'

df = pd.read_excel(archivo1, sheet_name='David')

dfPositivos = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])
dfNegativos = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])
dfNeutros = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])
dfSinSentimiento = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])


for i in range(len(df)):
    if type(df['tweet_analizar_siempre'].values[i])!=float:
        df['tweet_analizar_siempre'].values[i]=lt.limpiarTweets(df['tweet_analizar_siempre'].values[i])
    elif type(df['tweetnuevo_analiza_esta_primero'].values[i])!=float and type(df['tweetCitado_mirar_solo_si_hay_duda'].values[i])!=float:
        df['tweet_analizar_siempre'].values[i]=lt.limpiarTweets(df['tweetnuevo_analiza_esta_primero'].values[i]+df['tweetCitado_mirar_solo_si_hay_duda'].values[i])
    else:
        print("WTF")


for i in range(len(df)):
    if df['sentimiento'].values[i]==1:
        dfPositivos=dfPositivos.append(
            {'NumeroRetweets': df['NumeroRetweets'].values[i],
            'timestamp': df['timestamp'].values[i],
            'texto': df['tweet_analizar_siempre'].values[i],
            'sentimiento': df['sentimiento'].values[i]},
            ignore_index=True
            )
    elif df['sentimiento'].values[i]==-1:
        dfNegativos=dfNegativos.append(
            {'NumeroRetweets': df['NumeroRetweets'].values[i],
            'timestamp': df['timestamp'].values[i],
            'texto': df['tweet_analizar_siempre'].values[i],
            'sentimiento': df['sentimiento'].values[i]},
            ignore_index=True
            )
    elif df['sentimiento'].values[i]==0:
        dfNeutros=dfNeutros.append(
            {'NumeroRetweets': df['NumeroRetweets'].values[i],
            'timestamp': df['timestamp'].values[i],
            'texto': df['tweet_analizar_siempre'].values[i],
            'sentimiento': df['sentimiento'].values[i]},
            ignore_index=True
            )
    else:
        dfSinSentimiento=dfSinSentimiento.append(
            {'NumeroRetweets': df['NumeroRetweets'].values[i],
            'timestamp': df['timestamp'].values[i],
            'texto': df['tweet_analizar_siempre'].values[i],
            'sentimiento': df['sentimiento'].values[i]},
            ignore_index=True
            )


dfPositivos.to_excel("excelPositivosyo.xlsx")
dfNegativos.to_excel("excelNegativosyo.xlsx")
dfNeutros.to_excel("excelNeutrosyo.xlsx")
dfSinSentimiento.to_excel("excelSinSentimientoyo.xlsx")
