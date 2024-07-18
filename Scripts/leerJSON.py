#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

import json
import pandas as pd

df = pd.read_json('twitterCamposReducidos.json', dtype={'id_str': 'string'},encoding='UTF-8')

idUnicas = {}

contadorrtCitado=0
contadorrt=0
contadorCitado=0
contadorNormales=0
contadorNoContemplados=0
"""
Recorre el Dataframe donde está guardada la base de datos para eliminar los tweets duplicados y quedarse con el que tenga el mayor número de RTs
en el caso de encontrar un duplicado
"""
for i in range(len(df)):
    
    fecha=str(df['timestamp_ms'][i])
    
    #Si el tweet analizado es un retweet de un citado:
    if str(df['quoted_status'][i])!='nan' and str(df['retweeted_status'][i])!='nan':
        contadorrtCitado=contadorrtCitado+1
        numeroRT=df['retweeted_status'][i]['retweet_count']
        identificadorRT=str(df['retweeted_status'][i]['id_str'])

        #Si el ID del tweet no aparece en el diccionario:
        if str(identificadorRT) not in idUnicas:
            #Si el tanto el tweet como el citado están truncados:
            
            if df['retweeted_status'][i]['truncated']==True and df['quoted_status'][i]['truncated']==True:
                textoEnteroRT=df['retweeted_status'][i]['extended_tweet']['full_text']
                textoEnteroCitado=df['quoted_status'][i]['extended_tweet']['full_text']
                idUnicas.setdefault(identificadorRT,[numeroRT,textoEnteroRT,textoEnteroCitado,fecha])
            #Si el tweet está truncado pero el citado no:
            elif df['retweeted_status'][i]['truncated']==True and df['quoted_status'][i]['truncated']==False:
                textoEnteroRT=df['retweeted_status'][i]['extended_tweet']['full_text']
                textoCitado=df['quoted_status'][i]['text']
                idUnicas.setdefault(identificadorRT,[numeroRT,textoEnteroRT,textoCitado,fecha])
            #Si el citado está truncado pero el tweet no:
            elif df['retweeted_status'][i]['truncated']==False and df['quoted_status'][i]['truncated']==True:
                textoEnteroCitado=df['quoted_status'][i]['extended_tweet']['full_text']
                textoRT=df['retweeted_status'][i]['text']
                idUnicas.setdefault(identificadorRT,[numeroRT,textoRT,textoEnteroCitado,fecha])
            #Si ni el tweet ni el citado están truncados:
            else:
                textoCitado=df['quoted_status'][i]['text']
                textoRT=df['retweeted_status'][i]['text']
                idUnicas.setdefault(identificadorRT,[numeroRT,textoRT,textoCitado,fecha])
        #Si el ID del tweet ya está en el diccionario:
        else:
            #Comparo el número de retweets de ambos tweets y actualizo al mayor valor:
            if idUnicas.get(identificadorRT)[0]<numeroRT:
                idUnicas[identificadorRT][0]=numeroRT
    
    #Si el tweet analizado es un retweet:
    elif str(df['quoted_status'][i])=='nan' and str(df['retweeted_status'][i])!='nan':
        contadorrt=contadorrt+1
        
        numeroRT=df['retweeted_status'][i]['retweet_count']
        identificadorRT=str(df['retweeted_status'][i]['id_str'])
        
        #Si el ID del tweet no aparece en el diccionario:
        if identificadorRT not in idUnicas:
            #Si el retweet está truncado:
            if df['retweeted_status'][i]['truncated']==True:
                textoEnteroRT=df['retweeted_status'][i]['extended_tweet']['full_text']
                idUnicas.setdefault(identificadorRT,[numeroRT,textoEnteroRT,fecha])
            #Si el retweet no está truncado:
            else:
                textoRT=df['retweeted_status'][i]['text']
                idUnicas.setdefault(identificadorRT,[numeroRT,textoRT,fecha])
        #Si el ID del tweet ya está en el diccionario:
        else:
            #Comparo el número de retweets de ambos tweets y actualizo al mayor valor:
            if idUnicas.get(identificadorRT)[0]<numeroRT:
                idUnicas[identificadorRT][0]=numeroRT
    
    #Si el tweet analizado es un citado:        
    elif str(df['quoted_status'][i])!='nan' and str(df['retweeted_status'][i])=='nan':
        contadorCitado=contadorCitado+1
        identificadorNormal=str(df['id_str'][i])
        
        #Si el ID del tweet no aparece en el diccionario:
        if identificadorNormal not in idUnicas:
            #Si tanto el citado commo el nuevo están truncados:
            if df['quoted_status'][i]['truncated']==True and df['truncated'][i]==True:
                textoEnteroCitado=df['quoted_status'][i]['extended_tweet']['full_text']
                textoEnteroNormal=df['extended_tweet'][i]['full_text']
                #Primero guarda el tweet citado y después el nuevo:
                idUnicas.setdefault(identificadorNormal,[0,textoEnteroCitado,textoEnteroNormal,fecha])
            #Si el citado está truncado pero el nuevo no:
            elif df['quoted_status'][i]['truncated']==True and df['truncated'][i]==False:
                textoEnteroCitado=df['quoted_status'][i]['extended_tweet']['full_text']
                textoNormal=df['text'][i]
                idUnicas.setdefault(identificadorNormal,[0,textoEnteroCitado,textoNormal,fecha])
             #Si el citado no está truncado pero el nuevo si:
            elif df['quoted_status'][i]['truncated']==False and df['truncated'][i]==True:
                textoCitado=df['quoted_status'][i]['text']
                textoEnteroNormal=df['extended_tweet'][i]['full_text']
                idUnicas.setdefault(identificadorNormal,[0,textoCitado,textoEnteroNormal,fecha])
            #Si ninguno está truncado:
            else:
                textoCitado=df['quoted_status'][i]['text']
                textoNormal=df['text'][i]
                idUnicas.setdefault(identificadorNormal,[0,textoCitado,textoNormal,fecha])
            
    #Si el tweet analizado es un tweet normal:    
    elif str(df['quoted_status'][i])=='nan' and str(df['retweeted_status'][i])=='nan':
        contadorNormales=contadorNormales+1
        identificadorNormal=str(df['id_str'][i])
        
        #Si el ID del tweet no aparece en el diccionario:
        if identificadorNormal not in idUnicas:
            #Si el tweet está truncado:
            if df['truncated'][i]==True:
                textoEnteroNormal=df['extended_tweet'][i]['full_text']
                idUnicas.setdefault(identificadorNormal,[0,textoEnteroNormal,fecha])
            #Si el tweet no está truncado:
            else:
                textoNormal=df['text'][i]
                idUnicas.setdefault(identificadorNormal,[0,textoNormal,fecha])
            
    else:
        contadorNoContemplados=0
        
print("Numero de rt citados: ")
print(contadorrtCitado)
print("Numero de rt: ")
print(contadorrt)
print("Numero de citados: ")
print(contadorCitado)
print("Numero de normales: ")
print(contadorNormales)
print("Numero de no contemplados: ")
print(contadorNoContemplados)
print("Longitud del diccionario")
print(len(idUnicas))

data = {}
data['tweets'] = []

#El resultado se guarda en un archivo JSON
for iden in idUnicas:
    
    if len(idUnicas[iden])==4:
        data['tweets'].append({
        'Identificador': str(iden),    
        'NumeroRetweets': str(idUnicas[iden][0]),
        'tweetCitado': str(idUnicas[iden][1]),
        'tweetNuevo': str(idUnicas[iden][2]),
        'timestamp': str(idUnicas[iden][3]),
        'sentimiento': None})
    elif len(idUnicas[iden])==3:
        data['tweets'].append({
        'Identificador': str(iden),
        'NumeroRetweets': str(idUnicas[iden][0]),
        'tweet': str(idUnicas[iden][1]),
        'timestamp': str(idUnicas[iden][2]),
        'sentimiento': None})
    else:
        print("Error")
        
with open('prueba1.json', 'w',encoding='UTF-8') as file:
    json.dump(data, file, indent=4)
