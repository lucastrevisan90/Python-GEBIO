# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 23:06:16 2019

@author: lucas
"""
import time
import numpy as np
import cv2
start_time = time.time()


img = cv2.imread("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\Imagens-mais_recentes_cortadas\\crop_26.jpg") #carregando a imagem
linhas, colunas, _ = img.shape #criando duas variáveis com mesmas dimensões que a quantidade de linhas e colunas da imagem inicial (img)
    
img_folha = img #renomeando a imagem original tanto o calculo da area de referencia para encontrar tamanho de pixels
img_escala = img# quanto a area da folha serão baseadadas na img inicial, duas novas variáveis foram criadas com os mesmo valores de img
    
    
img2=np.zeros((linhas,colunas)) #img2 e img3 são imagens vazias de mesmas dimensões que a img original
img3=np.zeros((linhas,colunas))	
    
for k in range(linhas):
    for n in range(colunas):
        GB =((img_folha[[k],[n]][0][1])/((img_folha[[k],[n]][0][0])+0.0000001)) #coordenadas e respectivos valores dos canais verde(1) e azul(0)
        if GB <1.02: #threshold
            img_folha[[k],[n]]=255 #img_folha recebe o valor 0 na posição kxn - isso resulta em um fundo preto.Se quiser fundo branco, coloca 255 ou invés de 0			
        else:
            img_folha[[k],[n]] = img_folha[[k],[n]]#img_folha mantem a cor original na posição kxn
            		
            
cv2.imshow("Original", img_folha)
cv2.imwrite("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\imagens-mais_recentes_cortadas_semfundo\\crop_sf_94b.jpg", img_folha)
end_time = time.time()
print("Run time = {}".format(end_time - start_time))
    
cv2.waitKey()
cv2.destroyAllWindows() 
    	    