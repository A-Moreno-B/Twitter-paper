# -*- coding: utf-8 -*-

import pandas as pd

import matplotlib.pyplot as plt 


archivo = 'prueba2Clasificado.xlsx'

df = pd.read_excel(archivo, sheet_name='Sheet1')

        
"""        
Guarda los tweets de cada mes en un diccionario diferente donde la clave es el día y el valor asociado a cada clave la suma de 
los retweets que tienen los tweets de ese día
"""

def graficaFechas():
    
    dicEneroPos = {}
    dicFebreroPos = {}
    dicMarzoPos = {}
    dicAbrilPos = {}
    dicMayoPos = {}
    dicJunioPos = {}
    dicDiciembrePos = {}
    
    dicEneroNeg = {}
    dicFebreroNeg = {}
    dicMarzoNeg = {}
    dicAbrilNeg = {}
    dicMayoNeg = {}
    dicJunioNeg = {}
    dicDiciembreNeg = {}
    
    for i in range(len(df)):
        if df['sentimiento'].values[i]==1:
            if df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='1':
                if df['timestamp'].values[i][8:10] not in dicEneroPos.keys():
                    dicEneroPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicEneroPos.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicEneroPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicEneroPos[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='2':
                if df['timestamp'].values[i][8:10] not in dicFebreroPos.keys():
                    dicFebreroPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicFebreroPos.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicFebreroPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicFebreroPos[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='3':
                if df['timestamp'].values[i][8:10] not in dicMarzoPos.keys():
                     dicMarzoPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicMarzoPos.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicMarzoPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicMarzoPos[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='4':
                if df['timestamp'].values[i][8:10] not in dicAbrilPos.keys():
                     dicAbrilPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicAbrilPos.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicAbrilPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicAbrilPos[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='5':
                if df['timestamp'].values[i][8:10] not in dicMayoPos.keys():
                     dicMayoPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicMayoPos.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicMayoPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicMayoPos[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='6':
                if df['timestamp'].values[i][8:10] not in dicJunioPos.keys():
                    dicJunioPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicJunioPos.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicJunioPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicJunioPos[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='0' and df['timestamp'].values[i][5:7]=='12':
                if df['timestamp'].values[i][8:10] not in dicDiciembrePos.keys():
                    dicDiciembrePos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicDiciembrePos.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicDiciembrePos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicDiciembrePos[df['timestamp'].values[i][8:10]]+=1
                    
        elif df['sentimiento'].values[i]==-1:
            if df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='1':
                if df['timestamp'].values[i][8:10] not in dicEneroNeg.keys():
                     dicEneroNeg.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicEneroNeg.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicEneroNeg[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicEneroNeg[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='2':
                if df['timestamp'].values[i][8:10] not in dicFebreroNeg.keys():
                     dicFebreroNeg.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicFebreroNeg.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicFebreroNeg[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicFebreroNeg[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='3':
                if df['timestamp'].values[i][8:10] not in dicMarzoNeg.keys():
                     dicMarzoNeg.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicMarzoNeg.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicMarzoNeg[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicMarzoNeg[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='4':
                if df['timestamp'].values[i][8:10] not in dicAbrilNeg.keys():
                     dicAbrilNeg.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicAbrilNeg.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicAbrilNeg[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicAbrilNeg[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='5':
                if df['timestamp'].values[i][8:10] not in dicMayoNeg.keys():
                     dicMayoNeg.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicMayoNeg.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicMayoNeg[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicMayoNeg[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='6':
                if df['timestamp'].values[i][8:10] not in dicJunioNeg.keys():
                     dicJunioNeg.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicJunioNeg.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicJunioNeg[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicJunioNeg[df['timestamp'].values[i][8:10]]+=1
            elif df['timestamp'].values[i][3:4]=='0' and df['timestamp'].values[i][5:7]=='12':
                if df['timestamp'].values[i][8:10] not in dicDiciembreNeg.keys():
                     dicDiciembreNeg.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    #dicDiciembreNeg.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                     dicDiciembreNeg[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    #dicDiciembreNeg[df['timestamp'].values[i][8:10]]+=1
                   
                

    xEneroPos=list(dicEneroPos)
    xEneroPos.sort()
    yEneroPos=[]
    for j in range(len(xEneroPos)):
        yEneroPos.append(dicEneroPos[xEneroPos[j]])
        
    xFebreroPos=list(dicFebreroPos)
    xFebreroPos.sort()
    yFebreroPos=[]
    for j in range(len(xFebreroPos)):
        yFebreroPos.append(dicFebreroPos[xFebreroPos[j]])
        
    xMarzoPos=list(dicMarzoPos)
    xMarzoPos.sort()
    yMarzoPos=[]
    for j in range(len(xMarzoPos)):
        yMarzoPos.append(dicMarzoPos[xMarzoPos[j]])
        
    xAbrilPos=list(dicAbrilPos)
    xAbrilPos.sort()
    yAbrilPos=[]
    for j in range(len(xAbrilPos)):
        yAbrilPos.append(dicAbrilPos[xAbrilPos[j]])
        
    xMayoPos=list(dicMayoPos)
    xMayoPos.sort()
    yMayoPos=[]
    for j in range(len(xMayoPos)):
        yMayoPos.append(dicMayoPos[xMayoPos[j]])
        
    xJunioPos=list(dicJunioPos)
    xJunioPos.sort()
    yJunioPos=[]
    for j in range(len(xJunioPos)):
        yJunioPos.append(dicJunioPos[xJunioPos[j]])
        
    xDiciembrePos=list(dicDiciembrePos)
    xDiciembrePos.sort()
    yDiciembrePos=[]
    for j in range(len(xDiciembrePos)):
        yDiciembrePos.append(dicDiciembrePos[xDiciembrePos[j]])
        
    xEneroNeg=list(dicEneroNeg)
    xEneroNeg.sort()
    yEneroNeg=[]
    for j in range(len(xEneroNeg)):
        yEneroNeg.append(dicEneroNeg[xEneroNeg[j]])
        
    xFebreroNeg=list(dicFebreroNeg)
    xFebreroNeg.sort()
    yFebreroNeg=[]
    for j in range(len(xFebreroNeg)):
        yFebreroNeg.append(dicFebreroNeg[xFebreroNeg[j]])
        
    xMarzoNeg=list(dicMarzoNeg)
    xMarzoNeg.sort()
    yMarzoNeg=[]
    for j in range(len(xMarzoNeg)):
        yMarzoNeg.append(dicMarzoNeg[xMarzoNeg[j]])
        
    xAbrilNeg=list(dicAbrilNeg)
    xAbrilNeg.sort()
    yAbrilNeg=[]
    for j in range(len(xAbrilNeg)):
        yAbrilNeg.append(dicAbrilNeg[xAbrilNeg[j]])
        
    xMayoNeg=list(dicMayoNeg)
    xMayoNeg.sort()
    yMayoNeg=[]
    for j in range(len(xMayoNeg)):
        yMayoNeg.append(dicMayoNeg[xMayoNeg[j]])
        
    xJunioNeg=list(dicJunioNeg)
    xJunioNeg.sort()
    yJunioNeg=[]
    for j in range(len(xJunioNeg)):
        yJunioNeg.append(dicJunioNeg[xJunioNeg[j]])
        
    xDiciembreNeg=list(dicDiciembreNeg)
    xDiciembreNeg.sort()
    yDiciembreNeg=[]
    for j in range(len(xDiciembreNeg)):
        yDiciembreNeg.append(dicDiciembreNeg[xDiciembreNeg[j]])
        
    maximos=[max(yEneroPos),max(yFebreroPos),max(yMarzoPos),max(yAbrilPos),max(yMayoPos),max(yJunioPos),max(yDiciembrePos)]
    maximo=max(maximos)
    print(maximo)
    
    maximos2=[max(yEneroNeg),max(yFebreroNeg),max(yMarzoNeg),max(yAbrilNeg),max(yMayoNeg),max(yJunioNeg),max(yDiciembreNeg)]
    maximo2=max(maximos2)
    print(maximo2)
        
    pos, = plt.plot(xEneroPos,yEneroPos,marker="o",color='g',label="positives")
    plt.xlabel("Day", size = 14,)
    plt.ylabel("Number of RTs", size = 14)
    plt.title("January - 2021")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xEneroNeg,yEneroNeg,marker="o",color='r',label="negatives")
    plt.ylabel("Number of RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["positive", "negative"])
    plt.show()
    
    pos, = plt.plot(xFebreroPos,yFebreroPos,marker="o",color='g',label="positivos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Febrero")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xFebreroNeg,yFebreroNeg,marker="o",color='r',label="negativos")
    plt.ylabel("Tweets únicos", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["positivo", "negativo"])
    plt.show()
    
    pos, = plt.plot(xMarzoPos,yMarzoPos,marker="o",color='g',label="positivos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Marzo")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xMarzoNeg,yMarzoNeg,marker="o",color='r',label="negativos")
    plt.ylabel("Tweets únicos", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["positivo", "negativo"])
    plt.show()
    
    pos, = plt.plot(xAbrilPos,yAbrilPos,marker="o",color='g',label="positivos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Abril")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xAbrilNeg,yAbrilNeg,marker="o",color='r',label="negativos")
    plt.ylabel("Tweets únicos", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["positivo", "negativo"])
    plt.show()
    
    pos, = plt.plot(xMayoPos,yMayoPos,marker="o",color='g',label="positivos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Mayo")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xMayoNeg,yMayoNeg,marker="o",color='r',label="negativos")
    plt.ylabel("Tweets únicos", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["positivo", "negativo"])
    plt.show()
    
    pos, = plt.plot(xJunioPos,yJunioPos,marker="o",color='g',label="positives")
    plt.xlabel("Day", size = 14,)
    plt.ylabel("Number of RTs", size = 14)
    plt.title("June - 2021")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xJunioNeg,yJunioNeg,marker="o",color='r',label="negatives")
    plt.ylabel("Number of RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["positive", "negative"])
    plt.show()
    
    pos, = plt.plot(xDiciembrePos,yDiciembrePos,marker="o",color='g',label="positivos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Diciembre")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xDiciembreNeg,yDiciembreNeg,marker="o",color='r',label="negativos")
    plt.ylabel("Tweets únicos", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["positivo", "negativo"])
    plt.show()
        

graficaFechas()