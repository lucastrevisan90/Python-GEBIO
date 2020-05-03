# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:57:25 2020

@author: Lucas
"""


import pandas as pd
import numpy as np
from sklearn import svm

# Packages for visuals

import seaborn as sns; sns.set(font_scale=1.2)

#ler os dados usando pandas
data = pd.read_csv("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\Imagens_treinamento\\Pasta1.csv", encoding="utf-8", sep=";")
classifier = pd.read_csv("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\Imagens_classificador\\classificar_dados.csv", encoding="utf-8", sep=";")

#plotando os dados de interesse dentro do dataset
sns.lmplot('Contrast', 'Energy', data=data, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 20});

#selecionando os dados de interesse dentro do dataset e atribuindo labels
textures = data[['Contrast','Energy']]
type_label = np.where(data['Type']=='Saudavel', 0, 1)

data_features = data.columns.values[1:].tolist()

# Fit do modelo SVM
model = svm.SVC(kernel='linear')
model.fit(textures, type_label)


def saudavel_ou_doente(Contrast, Energy):
    if(model.predict([[Contrast, Energy]]))==0:
        print('folha saudável!')
    else:
        print('folha doente!')
        

x = np.array(classifier[['Contrast','Energy']])

for i in range(len(x)):
    saudavel_ou_doente(x[i][0],x[i][1])


