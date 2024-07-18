# -*- coding: utf-8 -*-

import pandas as pd

import matplotlib.pyplot as plt 


archivo = 'prueba2Clasificado.xlsx'

df = pd.read_excel(archivo, sheet_name='Sheet1')

def graficaFechas():
    
    dicEnero = {}
    dicFebrero = {}
    dicMarzo = {}
    dicAbril = {}
    dicMayo = {}
    dicJunio = {}
    dicDiciembre = {}
    
    for i in range(len(df)):
        if df['sentimiento'].values[i]==1:
            if df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='1':
                if df['timestamp'].values[i][8:10] not in dicEnero.keys():
                    dicEnero.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicEnero[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='2':
                if df['timestamp'].values[i][8:10] not in dicFebrero.keys():
                    dicFebrero.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicFebrero[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='3':
                if df['timestamp'].values[i][8:10] not in dicMarzo.keys():
                    dicMarzo.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicMarzo[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='4':
                if df['timestamp'].values[i][8:10] not in dicAbril.keys():
                    dicAbril.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicAbril[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='5':
                if df['timestamp'].values[i][8:10] not in dicMayo.keys():
                    dicMayo.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicMayo[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='6':
                if df['timestamp'].values[i][8:10] not in dicJunio.keys():
                    dicJunio.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicJunio[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='0' and df['timestamp'].values[i][5:7]=='12':
                if df['timestamp'].values[i][8:10] not in dicDiciembre.keys():
                    dicDiciembre.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicDiciembre[df['timestamp'].values[i][8:10]]+=1
                   

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
        
    maximos=[max(yEnero),max(yFebrero),max(yMarzo),max(yAbril),max(yMayo),max(yJunio),max(yDiciembre)]
    maximo=max(maximos)
    
        
    plt.plot(xEnero,yEnero,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Negativos enero")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xFebrero,yFebrero,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Negativos febrero")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xMarzo,yMarzo,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Negativos marzo")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xAbril,yAbril,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Negativos abril")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xMayo,yMayo,marker="o")
    plt.xlabel("Day", size = 14,)
    plt.ylabel("Unique tweets", size = 14)
    plt.title("May positives - 2021")
    plt.ylim(1800,max(yMayo)+50)
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xJunio,yJunio,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Negativos junio")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.show()
    
    plt.plot(xDiciembre,yDiciembre,marker="o")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Negativos diciembre")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.show()
        
    
    
# limpiarFecha()
graficaFechas()