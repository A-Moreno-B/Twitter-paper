# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import GaussianNB 

from sklearn.naive_bayes import ComplementNB

from sklearn.naive_bayes import MultinomialNB

from sklearn.naive_bayes import BernoulliNB

from sklearn.model_selection import train_test_split

from sklearn.svm import LinearSVC
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.datasets import make_classification

# from sklearn.linear_model import SGDClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import make_pipeline

from sklearn.model_selection import cross_val_score

# from sklearn.pipeline import make_pipeline

import pandas as pd

# from sklearn.metrics import recall_score

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix

from sklearn.metrics import accuracy_score

from sklearn import svm

import matplotlib.pyplot as plt 

from statsmodels.stats.multicomp import pairwise_tukeyhsd

import numpy as np

#from sklearn.metrics import plot_confusion_matrix

# from sklearn.preprocessing import StandardScaler

# from sklearn.model_selection import cross_validate

# import random

# from nltk import classify
# from nltk import NaiveBayesClassifier

from sklearn.linear_model import LogisticRegression

import statsmodels.api as sm

from statsmodels.formula.api import ols

# import sklearn

# from sklearn.ensemble import AdaBoostClassifier

# from sklearn.gaussian_process import GaussianProcessClassifier

# from sklearn.linear_model import PassiveAggressiveClassifier

archivoSinSen = 'prueba2SinSentimientos.xlsx'

archivoNeg = 'prueba2Negativos.xlsx'

archivoNeu = 'prueba2Neutros.xlsx'

archivoPos = 'prueba2Positivos.xlsx'

#Lee los archivos y guarda cada uno en un DataFrame

dfNeg = pd.read_excel(archivoNeg, sheet_name='Sheet1')

dfNeutro = pd.read_excel(archivoNeu, sheet_name='Sheet1')

dfPos = pd.read_excel(archivoPos, sheet_name='Sheet1')

#dfSinSen = pd.read_excel(archivoSinSen, sheet_name='Sheet1')

print("Longitud pos:")
print(dfPos.shape)
print("Longitud neg:")
print(dfNeg.shape)
print("Longitud neutro:")
print(dfNeutro.shape)

dataframes=[dfPos,dfNeg,dfNeutro]

dfUnion = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])

dfUnion=pd.concat(dataframes, sort=False, ignore_index=True)

#Crea el vectorizador y vectoriza los tweets
        
vectorizer = TfidfVectorizer(sublinear_tf=True,max_df=1.0)

vectorizado = vectorizer.fit_transform(dfUnion['texto'].values.astype('U'))



X = vectorizado
y = dfUnion['sentimiento']
#Separa los tweets entre los que van a ser usados para entrenar y los que van a ser usados para testeo  

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.119,random_state=67) BUENO

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.119,random_state=67)

# Algoritmos a comparar

algorithms = {

    'SVC': svm.SVC(kernel='rbf', C=10,random_state=3).fit(X_train.toarray(), y_train.values.ravel()),

    'LinearSVC': LogisticRegression(C=1.0,penalty='l2',random_state=1,solver="newton-cg",class_weight="balanced").fit(X_train.toarray(), y_train.values.ravel()),

    'MultinomialNB': MultinomialNB(alpha=0.08).fit(X_train.toarray(), y_train.values.ravel()),

    'BernouilliNB': BernoulliNB(alpha=0.59).fit(X_train.toarray(), y_train.values.ravel()),

    'ComplementNB': ComplementNB(alpha=0.59).fit(X_train.toarray(), y_train.values.ravel()),

    'GaussianNB': GaussianNB().fit(X_train.toarray(), y_train.values.ravel())

}

# algorithms = {

#     'SVC': svm.SVC(kernel='rbf', C=10,random_state=3).fit(X_train.toarray(), y_train.values.ravel()),

#     'LinearSVC': LogisticRegression(C=1.0,penalty='l2',random_state=1,solver="newton-cg",class_weight="balanced").fit(X_train.toarray(), y_train.values.ravel()),

    
# }

# Realizar validación cruzada y guardar los resultados

results = []

 

for name, algo in algorithms.items():

    accuracy = cross_val_score(algo, X_train.toarray(), y_train.values.ravel(), cv=5,scoring='accuracy')

    f1 = cross_val_score(algo, X_train.toarray(), y_train.values.ravel(), cv=5, scoring='f1_macro')

    precision = cross_val_score(algo, X_train.toarray(), y_train.values.ravel(), cv=5,scoring='precision_macro')

    recall = cross_val_score(algo, X_train.toarray(), y_train.values.ravel(), cv=5,scoring='recall_macro')

    for i in range(5):

        results.append([name, accuracy[i], f1[i], precision[i], recall[i]])

 

df = pd.DataFrame(results, columns=['Algorithm', 'Accuracy', 'F1_score','Precision', 'Recall'])

metrics = ['Accuracy', 'F1_score', 'Precision', 'Recall']

for metric in metrics:
       print(f"\nTukey HSD for {metric}:")
       tukey = pairwise_tukeyhsd(endog=df[metric],
                                 groups=df['Algorithm'],
                                 alpha=0.05)

       print(tukey)
       
       fig = tukey.plot_simultaneous()
       plt.title(f'Tukey HSD for {metric}')
       plt.tight_layout()
       plt.show()

fig, ax = plt.subplots(1,1)
ax.boxplot([df['Accuracy'],df['F1_score'],df['Precision'],df['Recall']])
ax.set_xticklabels(["Accuracy","F1_score","Precision","Recall"])
ax.set_ylabel("mean")
plt.show()

# Imprimir los resultados promedio por algoritmo

print(df.groupby('Algorithm').mean())

 

# ANOVA para Accuracy

model_accuracy = ols('Accuracy ~ C(Algorithm)', data=df).fit()

anova_table_accuracy = sm.stats.anova_lm(model_accuracy, typ=2)

print("ANOVA para Accuracy:\n", anova_table_accuracy)

 

# ANOVA para F1-score

model_f1 = ols('F1_score ~ C(Algorithm)', data=df).fit()

anova_table_f1 = sm.stats.anova_lm(model_f1, typ=2)

print("ANOVA para F1-score:\n", anova_table_f1)

 

# ANOVA para Precision

model_precision = ols('Precision ~ C(Algorithm)', data=df).fit()

anova_table_precision = sm.stats.anova_lm(model_precision, typ=2)

print("ANOVA para Precision:\n", anova_table_precision)

 

# ANOVA para Recall

model_recall = ols('Recall ~ C(Algorithm)', data=df).fit()

anova_table_recall = sm.stats.anova_lm(model_recall, typ=2)

print("ANOVA para Recall:\n", anova_table_recall)

#Crea el clasificador

#clf = MultinomialNB(alpha=0.08) 

#clf = GaussianNB() 
#clf=ComplementNB(alpha=0.59)

#clf = svm.SVC(kernel='rbf', C=10,random_state=3).fit(X_train, y_train)

#clf = BernoulliNB(alpha=0.59)  
#clf=LinearSVC(C=0.5)

#clf = LogisticRegression(C=1.0,penalty='l2',random_state=1,solver="newton-cg",class_weight="balanced") 58

#Para que el clasificador se ajuste al modelo debe aprender de él, por eso se llama al método fit

#clf.fit(X_train.toarray(), y_train.values.ravel())

#El clasificador predice los datos separados anteriormente para la fase de testeo

#predictions = clf.predict(X_test.toarray())

#Calcula la matriz de confusión y la precisión del clasificador

#print(classification_report(predictions, y_test))
#print('\n')
#print('Confusion matrix: \n', confusion_matrix(predictions, y_test))
#print('\n')
#print('Accuracy score: ', accuracy_score(predictions, y_test))
#print('\n\n\n')

#conf_matrix=confusion_matrix(predictions, y_test)
#print("----------------------------")
#print(conf_matrix[0][0])
#print("----------------------------")
#filaNeg=conf_matrix[0][0]+conf_matrix[0][1]+conf_matrix[0][2]
#filaNeu=conf_matrix[1][0]+conf_matrix[1][1]+conf_matrix[1][2]
#filaPos=conf_matrix[2][0]+conf_matrix[2][1]+conf_matrix[2][2]
#print(filaNeg)
#print(filaNeu)
#print(filaPos)
#print("----------------------------")
#ayuda=np.empty((3, 3))

#ayuda[0][0]=float(round(conf_matrix[0][0]/filaNeg,2))
#ayuda[0][1]=float(round(conf_matrix[0][1]/filaNeg,2))
#ayuda[0][2]=float(round(conf_matrix[0][2]/filaNeg,2))

#ayuda[1][0]=float(round(conf_matrix[1][0]/filaNeu,2))
#ayuda[1][1]=float(round(conf_matrix[1][1]/filaNeu,2))
#ayuda[1][2]=float(round(conf_matrix[1][2]/filaNeu,2))

#ayuda[2][0]=float(round(conf_matrix[2][0]/filaPos,2))
#ayuda[2][1]=float(round(conf_matrix[2][1]/filaPos,2))
#ayuda[2][2]=float(round(conf_matrix[2][2]/filaPos,2))


#fig, ax = plt.subplots(figsize=(7.5, 7.5))
#ax.matshow(ayuda, cmap=plt.cm.get_cmap('YlGn'), alpha=0.9)

#for i in range(ayuda.shape[0]):
#    for j in range(conf_matrix.shape[1]):
#        ax.text(x=j, y=i,s=ayuda[i, j], va='center', ha='center', size='xx-large')


#plt.xlabel('Predichos', fontsize=18)
#plt.ylabel('Reales', fontsize=18)
#plt.title('SVC', fontsize=18)
#plt.xticks([0,1,2], [-1,0,1],fontsize=18)
#plt.yticks([0,1,2], [-1,0,1],fontsize=18)
#plt.show()



#Predice el resto de tweets con el clasificador que acaba de crear

# dfAuxiliar = pd.DataFrame(columns=['NumeroRetweets','timestamp','texto','sentimiento'])

# for i in range(len(dfSinSen)):
#     #tweet=dfSinSen['texto'].values[i]
#     preprocess_tweet=str(dfSinSen['texto'].values[i])
#     #preprocess_tweet = lt.limpiarTweets(tweet)
#     tweet_vec = vectorizer.transform(pd.Series([preprocess_tweet]))
#     tweet_prediction = clf.predict(tweet_vec.toarray())

#     dfAuxiliar=dfAuxiliar.append(
#         {'NumeroRetweets': dfSinSen['NumeroRetweets'].values[i],
#         'timestamp': dfSinSen['timestamp'].values[i],
#         'texto': dfSinSen['texto'].values[i],
#         'sentimiento': tweet_prediction[0]},
#         ignore_index=True
#         )
   
# dfAuxiliar.to_excel("prueba2Clasificado.xlsx")
