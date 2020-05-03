# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:43:09 2020

@author: Lucas
"""


from skimage.feature import greycomatrix, greycoprops
from skimage import data
import matplotlib.pyplot as plt
import cv2


img1 = cv2.imread("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\imagens-mais_antigas_cortadas_semfundo\\cortada_sf_1.jpg", 0)
img2 = cv2.imread("C:\\Users\\Lucas\\Desktop\\Textura\\CONBAP\\imagens-mais_recentes_cortadas_semfundo\\crop_sf_2.jpg", 0)


imagens = (img1, img2)

cont = []
for i in range(len(imagens)):
    glcm = greycomatrix(imagens[i], [5], [50], 256, symmetric=True, normed=True)
    a = greycoprops(glcm, 'contrast')[0][0]
    cont.append(a)
    print(cont)

# cont = []
# diss = []
# homo = []
# ASM = []
# ener = []
# corr = []

# a = greycoprops(glcm, 'energy')[0][0]

# print(a)
# cv2.imshow('', img)

# cv2.waitKey()
# cv2.destroyAllWindows()
