# -*- coding: utf-8 -*-

import pandas as pd

archivo1 = 'paraClasificar.xlsx'

df = pd.read_excel(archivo1, sheet_name='Hoja1')

dfNegativos = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])

for i in range(len(df)):
    if type(df['tweet_analizar_siempre'].values[i])!=float:
        
        if 'yomevacuno' in df['tweet_analizar_siempre'].values[i].lower():
            print(df['tweet_analizar_siempre'].values[i])
            sentimiento = input('¿Es positivo?')
            if(sentimiento=='s'):
                df['sentimiento'].values[i]=1
                dfNegativos=dfNegativos.append(
                    {'NumeroRetweets': df['NumeroRetweets'].values[i],
                    'timestamp': df['timestamp'].values[i],
                    'texto': df['tweet_analizar_siempre'].values[i],
                    'sentimiento': df['sentimiento'].values[i]},
                    ignore_index=True
                    )
    elif type(df['tweetCitado_mirar_solo_si_hay_duda'].values[i])!=float:
        if 'yomevacuno' in df['tweetCitado_mirar_solo_si_hay_duda'].values[i].lower() :
            print(df['tweetCitado_mirar_solo_si_hay_duda'].values[i])
            sentimiento = input('¿Es positivo?')
            if(sentimiento=='s'):
                df['sentimiento'].values[i]=1
                dfNegativos=dfNegativos.append(
                    {'NumeroRetweets': df['NumeroRetweets'].values[i],
                    'timestamp': df['timestamp'].values[i],
                    'texto': df['tweetCitado_mirar_solo_si_hay_duda'].values[i]+df['tweetnuevo_analiza_esta_primero'].values[i],
                    'sentimiento': df['sentimiento'].values[i]},
                    ignore_index=True
                    )
    elif type(df['tweetnuevo_analiza_esta_primero'].values[i])!=float:
        if 'yomevacuno' in df['tweetnuevo_analiza_esta_primero'].values[i].lower():
            print(df['tweetnuevo_analiza_esta_primero'].values[i])
            sentimiento = input('¿Es positivo?')
            if(sentimiento=='s'):
                df['sentimiento'].values[i]=1
                dfNegativos=dfNegativos.append(
                    {'NumeroRetweets': df['NumeroRetweets'].values[i],
                    'timestamp': df['timestamp'].values[i],
                    'texto': df['tweetCitado_mirar_solo_si_hay_duda'].values[i]+df['tweetnuevo_analiza_esta_primero'].values[i],
                    'sentimiento': df['sentimiento'].values[i]},
                    ignore_index=True
                    )
                
                
                
dfNegativos.to_excel("excelClasificadosPrograma.xlsx")