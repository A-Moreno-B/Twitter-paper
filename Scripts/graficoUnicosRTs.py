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
    
    dicEneroUnico = {}
    dicFebreroUnico = {}
    dicMarzoUnico = {}
    dicAbrilUnico = {}
    dicMayoUnico = {}
    dicJunioUnico = {}
    dicDiciembreUnico = {}
    
    dicEneroRT = {}
    dicFebreroRT = {}
    dicMarzoRT = {}
    dicAbrilRT = {}
    dicMayoRT = {}
    dicJunioRT = {}
    dicDiciembreRT = {}
    
    for i in range(len(df)):
        if df['sentimiento'].values[i]==0:
            if df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='1':
                if df['timestamp'].values[i][8:10] not in dicEneroUnico.keys():
                    dicEneroUnico.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    dicEneroUnico[df['timestamp'].values[i][8:10]]+=1
                    
                if df['timestamp'].values[i][8:10] not in dicEneroRT.keys():
                    dicEneroRT.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicEneroRT[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='2':
                if df['timestamp'].values[i][8:10] not in dicFebreroUnico.keys():
                    #dicFebreroPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    dicFebreroUnico.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    # dicFebreroPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    dicFebreroUnico[df['timestamp'].values[i][8:10]]+=1
                
                if df['timestamp'].values[i][8:10] not in dicFebreroRT.keys():
                    dicFebreroRT.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicFebreroRT[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='3':
                if df['timestamp'].values[i][8:10] not in dicMarzoUnico.keys():
                    # dicMarzoPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    dicMarzoUnico.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    # dicMarzoPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    dicMarzoUnico[df['timestamp'].values[i][8:10]]+=1
                    
                if df['timestamp'].values[i][8:10] not in dicMarzoRT.keys():
                    dicMarzoRT.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicMarzoRT[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='4':
                if df['timestamp'].values[i][8:10] not in dicAbrilUnico.keys():
                    # dicAbrilPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    dicAbrilUnico.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    # dicAbrilPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    dicAbrilUnico[df['timestamp'].values[i][8:10]]+=1
                    
                if df['timestamp'].values[i][8:10] not in dicAbrilRT.keys():
                    dicAbrilRT.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicAbrilRT[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='5':
                if df['timestamp'].values[i][8:10] not in dicMayoUnico.keys():
                    # dicMayoPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    dicMayoUnico.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    # dicMayoPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    dicMayoUnico[df['timestamp'].values[i][8:10]]+=1
                    
                if df['timestamp'].values[i][8:10] not in dicMayoRT.keys():
                    dicMayoRT.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicMayoRT[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='1' and df['timestamp'].values[i][6:7]=='6':
                if df['timestamp'].values[i][8:10] not in dicJunioUnico.keys():
                    #dicJunioPos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    dicJunioUnico.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    # dicJunioPos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    dicJunioUnico[df['timestamp'].values[i][8:10]]+=1
                    
                if df['timestamp'].values[i][8:10] not in dicJunioRT.keys():
                    dicJunioRT.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicJunioRT[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
            elif df['timestamp'].values[i][3:4]=='0' and df['timestamp'].values[i][5:7]=='12':
                if df['timestamp'].values[i][8:10] not in dicDiciembreUnico.keys():
                    #dicDiciembrePos.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                    dicDiciembreUnico.setdefault(df['timestamp'].values[i][8:10],1)
                else:
                    # dicDiciembrePos[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                    dicDiciembreUnico[df['timestamp'].values[i][8:10]]+=1
                    
                if df['timestamp'].values[i][8:10] not in dicDiciembreRT.keys():
                    dicDiciembreRT.setdefault(df['timestamp'].values[i][8:10],int(df['NumeroRetweets'].values[i]))
                else:
                    dicDiciembreRT[df['timestamp'].values[i][8:10]]+=int(df['NumeroRetweets'].values[i])
                                  

    xEneroPos=list(dicEneroUnico)
    xEneroPos.sort()
    yEneroPos=[]
    for j in range(len(xEneroPos)):
        yEneroPos.append(dicEneroUnico[xEneroPos[j]])
        
    xFebreroPos=list(dicFebreroUnico)
    xFebreroPos.sort()
    yFebreroPos=[]
    for j in range(len(xFebreroPos)):
        yFebreroPos.append(dicFebreroUnico[xFebreroPos[j]])
        
    xMarzoPos=list(dicMarzoUnico)
    xMarzoPos.sort()
    yMarzoPos=[]
    for j in range(len(xMarzoPos)):
        yMarzoPos.append(dicMarzoUnico[xMarzoPos[j]])
        
    xAbrilPos=list(dicAbrilUnico)
    xAbrilPos.sort()
    yAbrilPos=[]
    for j in range(len(xAbrilPos)):
        yAbrilPos.append(dicAbrilUnico[xAbrilPos[j]])
        
    xMayoPos=list(dicMayoUnico)
    xMayoPos.sort()
    yMayoPos=[]
    for j in range(len(xMayoPos)):
        yMayoPos.append(dicMayoUnico[xMayoPos[j]])
        
    xJunioPos=list(dicJunioUnico)
    xJunioPos.sort()
    yJunioPos=[]
    for j in range(len(xJunioPos)):
        yJunioPos.append(dicJunioUnico[xJunioPos[j]])
        
    xDiciembrePos=list(dicDiciembreUnico)
    xDiciembrePos.sort()
    yDiciembrePos=[]
    for j in range(len(xDiciembrePos)):
        yDiciembrePos.append(dicDiciembreUnico[xDiciembrePos[j]])
        
    xEneroNeg=list(dicEneroRT)
    xEneroNeg.sort()
    yEneroNeg=[]
    for j in range(len(xEneroNeg)):
        yEneroNeg.append(dicEneroRT[xEneroNeg[j]])
        
    xFebreroNeg=list(dicFebreroRT)
    xFebreroNeg.sort()
    yFebreroNeg=[]
    for j in range(len(xFebreroNeg)):
        yFebreroNeg.append(dicFebreroRT[xFebreroNeg[j]])
        
    xMarzoNeg=list(dicMarzoRT)
    xMarzoNeg.sort()
    yMarzoNeg=[]
    for j in range(len(xMarzoNeg)):
        yMarzoNeg.append(dicMarzoRT[xMarzoNeg[j]])
        
    xAbrilNeg=list(dicAbrilRT)
    xAbrilNeg.sort()
    yAbrilNeg=[]
    for j in range(len(xAbrilNeg)):
        yAbrilNeg.append(dicAbrilRT[xAbrilNeg[j]])
        
    xMayoNeg=list(dicMayoRT)
    xMayoNeg.sort()
    yMayoNeg=[]
    for j in range(len(xMayoNeg)):
        yMayoNeg.append(dicMayoRT[xMayoNeg[j]])
        
    xJunioNeg=list(dicJunioRT)
    xJunioNeg.sort()
    yJunioNeg=[]
    for j in range(len(xJunioNeg)):
        yJunioNeg.append(dicJunioRT[xJunioNeg[j]])
        
    xDiciembreNeg=list(dicDiciembreRT)
    xDiciembreNeg.sort()
    yDiciembreNeg=[]
    for j in range(len(xDiciembreNeg)):
        yDiciembreNeg.append(dicDiciembreRT[xDiciembreNeg[j]])
        
    maximos=[max(yEneroPos),max(yFebreroPos),max(yMarzoPos),max(yAbrilPos),max(yMayoPos),max(yJunioPos),max(yDiciembrePos)]
    maximo=max(maximos)
    print(maximo)
    
    maximos2=[max(yEneroNeg),max(yFebreroNeg),max(yMarzoNeg),max(yAbrilNeg),max(yMayoNeg),max(yJunioNeg),max(yDiciembreNeg)]
    maximo2=max(maximos2)
    print(maximo2)
        
    pos, = plt.plot(xEneroPos,yEneroPos,marker="o",color='orange',label="Unique tweets")
    plt.xlabel("Day", size = 14,)
    plt.ylabel("Unique tweets", size = 14)
    plt.title("January neutres - 2021")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xEneroNeg,yEneroNeg,marker="o",color='brown',label="Número de RTs")
    plt.ylabel("Number of RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["Unique tweets", "Number of RTs"])
    plt.show()
    
    pos, = plt.plot(xFebreroPos,yFebreroPos,marker="o",color='orange',label="Tweets únicos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Neutros febrero")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xFebreroNeg,yFebreroNeg,marker="o",color='brown',label="Número de RTs")
    plt.ylabel("Número de RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["Tweets únicos", "Número de RTs"])
    plt.show()
    
    pos, = plt.plot(xMarzoPos,yMarzoPos,marker="o",color='orange',label="Tweets únicos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Neutros marzo")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xMarzoNeg,yMarzoNeg,marker="o",color='brown',label="Número de RTs")
    plt.ylabel("Número de RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["Tweets únicos", "Número de RTs"])
    plt.show()
    
    pos, = plt.plot(xAbrilPos,yAbrilPos,marker="o",color='orange',label="Tweets únicos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Neutros abril")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xAbrilNeg,yAbrilNeg,marker="o",color='brown',label="Número de RTs")
    plt.ylabel("Número de RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["Tweets únicos", "Número de RTs"])
    plt.show()
    
    pos, = plt.plot(xMayoPos,yMayoPos,marker="o",color='orange',label="Tweets únicos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Neutros mayo")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xMayoNeg,yMayoNeg,marker="o",color='brown',label="Número de RTs")
    plt.ylabel("Número de RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["Tweets únicos", "Número de RTs"])
    plt.show()
    
    pos, = plt.plot(xJunioPos,yJunioPos,marker="o",color='orange',label="Tweets únicos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Neutros junio")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xJunioNeg,yJunioNeg,marker="o",color='brown',label="Número de RTs")
    plt.ylabel("Número de RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["Tweets únicos", "Número de RTs"])
    plt.show()
    
    pos, = plt.plot(xDiciembrePos,yDiciembrePos,marker="o",color='orange',label="Tweets únicos")
    plt.xlabel("Día", size = 14,)
    plt.ylabel("Tweets únicos", size = 14)
    plt.title("Neutros diciembre")
    plt.ylim(0,maximo)
    plt.gcf().set_size_inches(9, 7)
    plt.twinx()
    neg, = plt.plot(xDiciembreNeg,yDiciembreNeg,marker="o",color='brown',label="Número de RTs")
    plt.ylabel("Número de RTs", size = 14)
    plt.ylim(0,maximo2)
    plt.legend([pos, (pos, neg)], ["Tweets únicos", "Número de RTs"])
    plt.show()
        

graficaFechas()