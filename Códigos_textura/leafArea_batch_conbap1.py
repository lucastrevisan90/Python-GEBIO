# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 23:06:16 2019

@author: lucas
"""
import time
import numpy as np
import cv2
start_time = time.time()


for i in range (1,129):
    img = cv2.imread("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\Imagens-mais_recentes_cortadas\\crop_26.jpg") #carregando a imagem
    linhas, colunas, _ = img.shape #criando duas variáveis com mesmas dimensões que a quantidade de linhas e colunas da imagem inicial (img)
    
    img_folha = img #renomeando a imagem original tanto o calculo da area de referencia para encontrar tamanho de pixels
    img_escala = img# quanto a area da folha serão baseadadas na img inicial, duas novas variáveis foram criadas com os mesmo valores de img
    img_folha = cv2.GaussianBlur(img_folha,(1,1),cv2.BORDER_WRAP ) #suaviza as imagens, pré processamento
    img_escala = cv2.GaussianBlur(img_escala,(1,1),cv2.BORDER_WRAP )
    
    img2=np.zeros((linhas,colunas)) #img2 e img3 são imagens vazias de mesmas dimensões que a img original
    img3=np.zeros((linhas,colunas))	
    
    for k in range(linhas):
    	for n in range(colunas):
    		GB =((img_folha[[k],[n]][0][1])/((img_folha[[k],[n]][0][0])+0.0000001)) #coordenadas e respectivos valores dos canais verde(1) e azul(0)
    		RB = ((img_escala[[k],[n]][0][2])/((img_escala[[k],[n]][0][0])+0.0000001))##coordenadas e respectivos valores dos canais vermelho(2) e azul(0)
    		if GB <1.2: #threshold
    			img_folha[[k],[n]]=0 #img_folha recebe o valor 0 na posição kxn
    			img2[[k],[n]]=0 #img2 = recebe o valor 0 na posição kxn
    		else:
    			img_folha[[k],[n]] = img_folha[[k],[n]] #img_folha mantem a cor original na posição kxn
    			img2[[k],[n]]=255 #img2 recebe valor máximo na posição kxn
    		if RB >1.2: #threshold
    			img_escala[[k],[n]]=0 #img_escala mantem a cor original na posição kxn
    			img3[[k],[n]]=0 #img3 mantem a cor original na posição kxn
    		else:
    			img_escala[[k],[n]] = img[[k],[n]] #img_escala mantem a cor original na posição kxn
    			img3[[k],[n]]=255	#img2 recebe valor máximo na posição kxn

	
    '''
    as imagens img_folha e img_escala são utilizadas para exibição das segmentações
    as imagens img2 e img3 são de fato utilizadas nos cálculos.
    '''
    
    # #########Esta parte se refere ao cálculo da área da escala
    escala = np.uint8(img3)	#converte a imagem img3 gerada anteriormente para uma imagem uint8
    
    area_folha = np.uint8(img2)	#converntendo img2 em uint8
    
    
    img_comb = img_folha + img_escala #combina as imagens da img_folha e da img_escala, as quais são as imagens segmentadas da folha e da escala separadas, apresentando, prespectivamente, a folha e a escala com o fundo removido e mantendo as cores originais (ilustração)
    
    #cv2.imshow("Original2", img_escala)
    #cv2.imshow('escala', escala)	
    cv2.imshow("Original", img_folha)
    #cv2.imshow('folha', area_folha)	
    #cv2.imshow('final', img_comb)
    
    print('')
    print('')
    print('')
    end_time = time.time()
    print("Run time = {}".format(end_time - start_time))
    
    cv2.waitKey(10)
    cv2.destroyAllWindows() 
    	