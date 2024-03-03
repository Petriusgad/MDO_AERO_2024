#####################################################################################
#------------Codigo desenvolvido por Paulo Robson - Fevereiro de 2024---------------#
#####################################################################################

import numpy as np


def asa_eliptica(c,b):
    # FUNÇÃO DE PI À POTÊNCIA 0.5^i (valores em radiano)
    p = 0 #power function
    posi_b = 0 #posição na envergadura
    parametro1 = []
    parametro2 = []
    span_points = []
    for i in range(1,6): # 5 seções (desconsiderando a raiz)
        p = (1/(2 ** i))
        posi_b += p
        span_points.append(posi_b * b) # posi_b é função para o circulo unitário
        theta1 = np.arccos(posi_b) # angulos no primeiro quadrante
        parametro1.insert(0,theta1)
        theta2 = 2 * np.pi - theta1 # angulos no quarto quadrante
        parametro2.append(theta2)
    span_points.insert(0,0.0) # insere o valor 0 no inicio da lista (posição inicial)
    Span = list(np.round(span_points, 4))

    parametro1.append(np.arccos(0)) # insere o valor para a posição 0 ja que a função não calcula
    parametro2.insert(0,2 * np.pi - np.arccos(0)) # aqui tambem insere o 0

    x1 = b * np.cos(parametro1)
    y1 = c * np.sin(parametro1) # 1/4 superior da corda

    x2 = b * np.cos(parametro2)
    y2 = 3 * c * np.sin(parametro2) # 3/4 inferior da corda

    #corda
    y1reversed = []
    for j in reversed(range(0,6)):
        y1reversed.append(y1[j])
    corda = []
    for k in range(0,6):
        corda.append(y1reversed[k] + abs(y2[k]))
    chord = list(np.round(corda, 4))

    # OFFSET = Xi - X1
    x_shifter = []
    for n in range(0,6):
        x_shifter.append(y1[n] - y1[0])
    offset = list(np.round(x_shifter, 4))  # kkkk "deslocador" coloquei isso só pra mudar o nome

    # CALCULAR A ÁREA DA MEIA ASA formula --> trapézio = (B + b)*h/2
    S = 0
    h = 0
    S_total = 0
    for z in range(0,5):
        S = (chord[z] + chord[z+1]) * (Span[z+1] - h) / 2
        h = Span[z+1]
        S_total += S # Area total da meia asa
    area = S_total * 2
    
    # Alongamento
    alon = ((Span[5]*2) ** 2) / (area) # Span(asa)^2/Area(asa) ASA INTEIRA

    return Span, chord, offset, area, alon

