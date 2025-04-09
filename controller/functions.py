import flet as ft
import numpy as np

def calcular_media(box_valores, valores, page, r): #parametros: input dos valores, valores, pagina, resposta
    lista_valores = [float(x)for x in valores.split()]
    arr_valores = np.array(lista_valores)
    media_valores = arr_valores.mean() #calcula a media dos valores

    r.value = f'a média dos valores é: {media_valores}'
    box_valores.value = f'' #limpa o input para valores futuros
    page.update()
   
    
def calcular_mediana(box_valores, valores, page, r): #parametros: input dos valores, valores, pagina, resposta
    lista_valores = [float(x)for x in valores.split()]
    arr_valores = np.array(lista_valores)
    mediana_valores = np.median(arr_valores) #calcula a mediana dos valores

    r.value = f'a mediana dos valores é: {mediana_valores}'
    box_valores.value = f'' #limpa o input para valores futuros
    page.update()
    

def calcular_desvio_padrao(box_valores, valores, page, r): #parametros: input dos valores, valores, pagina, resposta
    lista_valores = [float(x)for x in valores.split()]
    arr_valores = np.array(lista_valores)
    desvio_padrão = np.std(arr_valores) #calcula o desvio padrão dos valores

    r.value = f'o desvio padrão dos valores é: {desvio_padrão}'
    box_valores.value = f'' #limpa o input para valores futuros
    page.update()

def calcular_quartis(box_valores, valores, page, r): #parametros: input dos valores, valores, pagina, resposta
    lista_valores = [float(x)for x in valores.split()]
    arr_valores = np.array(lista_valores)
    q1 = np.percentile(arr_valores, 25) #calcula o primeiro quartil
    q2 = np.percentile(arr_valores, 50) #calcula o segundo quartil
    q3 = np.percentile(arr_valores, 75) #calcula o terceiro quartil

    r.value = f'Primeiro Quartil (Q1): {q1}\nSegundo Quartil (Q2): {q2}\nTerceiro Quartil(Q3): {q3}'
    box_valores.value = f'' #limpa o input para valores futuros
    page.update()

def calcular_variancia(box_valores, valores, page, r): #parametros: input dos valores, valores, pagina, resposta
    lista_valores = [float(x)for x in valores.split()]
    arr_valores = np.array(lista_valores)
    variancia = np.var(arr_valores) #calcula a variancia dos valores

    r.value = f'a variância dos valores é: {variancia}'
    box_valores.value = f'' #limpa o input para valores futuros
    page.update()
