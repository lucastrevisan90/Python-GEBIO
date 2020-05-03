# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:43:23 2020

@author: Lucas
"""


import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\imagens-mais_antigas_cortadas_semfundo\\ex_1.png")

 
altura, largura, _ = img.shape

imagemVazia=np.zeros((altura, largura), dtype='uint8') 

canalAzul, canalVerde, canalVermelho = cv2.split(img)   
Vermelho= cv2.merge([imagemVazia, imagemVazia, canalVermelho])     
Verde= cv2.merge([imagemVazia, canalVerde, imagemVazia])     
Azul= cv2.merge([canalAzul, imagemVazia, imagemVazia])
	 
 
avg_color1 = np.mean(canalVerde, axis=None) 
avg_color2 = np.mean(canalVermelho, axis=None)
avg_color3 = np.mean(canalAzul, axis=None)

MPRI_calc = (avg_color1 - avg_color2)/(avg_color1 + avg_color2) 
Gn_calc = (avg_color1)/(avg_color1 + avg_color2 + avg_color3) 
Rn_calc = (avg_color2)/(avg_color1 + avg_color2 + avg_color3) 
Bn_calc = (avg_color3)/(avg_color1 + avg_color2 + avg_color3) 
	
res = [MPRI_calc, Gn_calc, Rn_calc, Bn_calc]


print('MPRI =', MPRI_calc)
print('Gn =', Gn_calc)
print('Rn =', Rn_calc)
print('Bn =', Bn_calc)
	
print(MPRI_calc)
print(Gn_calc)
print(Rn_calc)
print(Bn_calc)

cv2.imshow('original', img)
cv2.imshow('AZUL', Azul)
cv2.imshow('VERDE', Verde)
cv2.imshow('VERMELHO', Vermelho)
cv2.waitKey(0)
cv2.destroyAllWindows()