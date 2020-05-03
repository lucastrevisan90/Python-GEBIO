# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:08:29 2020

@author: Lucas
"""


from skimage.feature import greycomatrix, greycoprops
from skimage import data
import matplotlib.pyplot as plt
import cv2
import glob
import pandas as pd


#lê uma lista de imagens
imagens = glob.glob("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\Imagens_treinamento\\saudaveis\\*.jpg")

#cria os vetores para armazenaros resultados das texturas
cont = []
diss = []
homo = []
ASM = []
ener = []
corr = []

texturas = []

#varre o vetor de imagens (pasta no diretório
for imagem in imagens:
    img = cv2.imread(imagem,0) #lê a imagem da respectiva iteração
    glcm = greycomatrix(img, [2], [0], 256, symmetric=True, normed=True) #calcula GLCM
    
    #calculos de todos os indices de textura
    contrast = greycoprops(glcm, 'contrast')[0][0]
    dissimilarity = greycoprops(glcm, 'dissimilarity')[0][0]
    homogeneity = greycoprops(glcm, 'homogeneity')[0][0]
    energy = greycoprops(glcm, 'energy')[0][0]
    correlation = greycoprops(glcm, 'correlation')[0][0]
    
    
       #append nos respectivos vetores
    cont.append(contrast)
    diss.append(dissimilarity)
    homo.append(homogeneity)
    ener.append(energy)
    corr.append(correlation)
    
    
    res = [contrast, dissimilarity, homogeneity, energy, correlation]
    texturas.append(res)
 

"""transforma a lista indices em um DataFrame"""
df = pd.DataFrame(texturas, columns = ['cont', 'diss', 'homo', 'ener', 'corr'])
df.index = df.index + 1
"""exportando dados em CSV"""
cvs_file = df.to_csv("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\resultados textura csv\\saudaveis_tex2.csv", sep=';')
print(df)