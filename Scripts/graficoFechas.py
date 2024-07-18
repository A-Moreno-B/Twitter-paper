# -*- coding: utf-8 -*-

import pandas as pd

import matplotlib.pyplot as plt 


archivo = 'prueba2Clasificado.xlsx'

df = pd.read_excel(archivo, sheet_name='Sheet1')

"""
Guarda la fecha en formato año-mes-día eliminando la hora. minutos y segundos
"""

def limpiarFecha():
    dfFechas = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])
    for i in range(len(df)):
        #df['timestamp'].values[i]=df['timestamp'].values[i][0:10]
        dfFechas=dfFechas.append(
            {'NumeroRetweets': df['NumeroRetweets'].values[i],
            'timestamp': df['timestamp'].values[i][0:10],
            'texto': df['texto'].values[i],
            'sentimiento': df['sentimiento'].values[i]},
            ignore_index=True
            )
    dfFechas.to_excel("excelFechas.xlsx")    
        
"""        
Guarda los tweets de cada mes en un diccionario diferente donde la clave es el día y el valor asociado a cada clave la suma de 
los retweets que tienen los tweets de ese día
"""

def graficaFechas():
    
    dicEnero = {}
    dicFebrero = {}
    dicMarzo = {}
    dicAbril = {}
    dicMayo = {}
    dicJunio = {}
    # dicJulio = {}
    # dicAgosto = {}
    # dicSeptiembre = {}
    # dicOctubre = {}
    # dicNoviembre = {}
    dicDiciembre = {}
    
    for i in range(len(df)):
        if df['sentimiento'].values[i]==-1:
            if df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='1':
                if df['timestamp'].values[i][8:10] not in dicEnero.keys():
                    dicEnero.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicEnero[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='2':
                if df['timestamp'].values[i][8:10] not in dicFebrero.keys():
                    dicFebrero.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicFebrero[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='3':
                if df['timestamp'].values[i][8:10] not in dicMarzo.keys():
                    dicMarzo.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicMarzo[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='4':
                if df['timestamp'].values[i][8:10] not in dicAbril.keys():
                    dicAbril.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicAbril[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='5':
                if df['timestamp'].values[i][8:10] not in dicMayo.keys():
                    dicMayo.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicMayo[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='6':
                if df['timestamp'].values[i][8:10] not in dicJunio.keys():
                    dicJunio.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicJunio[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                   elif df['timestamp'].values[i][3:4]=='0' and df['timestamp'].values[i][5:7]=='12':
                if df['timestamp'].values[i][8:10] not in dicDiciembre.keys():
                    dicDiciembre.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicDiciembre[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                   
                

    xEnero=list(dicEnero)
    xEnero.sort()
    yEnero=[]
    for j in range(len(xEnero)):
        yEnero.append(dicEnero[xEnero[j]])
        
    xFebrero=list(dicFebrero)
    xFebrero.sort()
    yFebrero=[]
    for j in range(len(xFebrero)):
        yFebrero.append(dicFebrero[xFebrero[j]])
        
    xMarzo=list(dicMarzo)
    xMarzo.sort()
    yMarzo=[]
    for j in range(len(xMarzo)):
        yMarzo.append(dicMarzo[xMarzo[j]])
        
    xAbril=list(dicAbril)
    xAbril.sort()
    yAbril=[]
    for j in range(len(xAbril)):
        yAbril.append(dicAbril[xAbril[j]])
        
    xMayo=list(dicMayo)
    xMayo.sort()
    yMayo=[]
    for j in range(len(xMayo)):
        yMayo.append(dicMayo[xMayo[j]])
        
    xJunio=list(dicJunio)
    xJunio.sort()
    yJunio=[]
    for j in range(len(xJunio)):
        yJunio.append(dicJunio[xJunio[j]])
        
    
        
    xDiciembre=list(dicDiciembre)
    xDiciembre.sort()
    yDiciembre=[]
    for j in range(len(xDiciembre)):
        yDiciembre.append(dicDiciembre[xDiciembre[j]])
    
        
    plt.plot(xEnero,yEnero,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Número de RTs", size = 14)
    plt.title("Enero")
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xFebrero,yFebrero,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Número de RTs", size = 14)
    plt.title("Febrero")
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xMarzo,yMarzo,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Número de RTs", size = 14)
    plt.title("Marzo")
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xAbril,yAbril,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Número de RTs", size = 14)
    plt.title("Abril")
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xMayo,yMayo,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Número de RTs", size = 14)
    plt.title("Mayo")
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xJunio,yJunio,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Número de RTs", size = 14)
    plt.title("Junio")
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    # plt.plot(xJulio,yJulio,marker="o")
    # plt.xlabel("Día", size = 14,)
    # plt.ylabel("Número de RTs", size = 14)
    # plt.title("Julio")
    # plt.gcf().set_size_inches(9, 7)
    # plt.show()
    
    # plt.plot(xAgosto,yAgosto,marker="o")
    # plt.xlabel("Día", size = 14,)
    # plt.ylabel("Número de RTs", size = 14)
    # plt.title("Agosto")
    # plt.gcf().set_size_inches(9, 7)
    # plt.show()
    
    # plt.plot(xSeptiembre,ySeptiembre,marker="o")
    # plt.xlabel("Día", size = 14,)
    # plt.ylabel("Número de RTs", size = 14)
    # plt.title("Septiembre")
    # plt.gcf().set_size_inches(9, 7)
    # plt.show()
    
    # plt.plot(xOctubre,yOctubre,marker="o")
    # plt.xlabel("Día", size = 14,)
    # plt.ylabel("Número de RTs", size = 14)
    # plt.title("Octubre")
    # plt.gcf().set_size_inches(9, 7)
    # plt.show()
    
    # plt.plot(xNoviembre,yNoviembre,marker="o")
    # plt.xlabel("Día", size = 14,)
    # plt.ylabel("Número de RTs", size = 14)
    # plt.title("Noviembre")
    # plt.gcf().set_size_inches(9, 7)
    # plt.show()
    
    plt.plot(xDiciembre,yDiciembre,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Número de RTs", size = 14)
    plt.title("Diciembre")
    plt.gcf().set_size_inches(9, 7)
    plt.show()
        
    
    
# limpiarFecha()
graficaFechas()



















