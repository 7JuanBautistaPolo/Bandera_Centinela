# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:15:02 2023

@author: Bautista Polo
"""

# Bandera/Centinela: hace la parada cuando se cumple la condicion de aprobado
def aprobar_propuesta (lista_votos):
    mayoria_absoluta = len(lista_votos)//2 + 1
    indice = 0
    centinela = True
    votos_favor = 0
    while centinela:
        if lista_votos[indice]:
            votos_favor   = votos_favor + 1
            indice  = indice + 1
            centinela = indice < len(lista_votos) and votos_favor < mayoria_absoluta # Aca aun no aprueba, debe seguir
            
        
    if votos_favor >= mayoria_absoluta: # Por que termino el recorrido?, por que se cumple la condicion
        return True
    else:
        return False
#%%
# Bandera/Centinela_2
def aprobar_propuesta_2 (lista_votos):
    mayoria_absoluta = len(lista_votos)//2 + 1
    votos_favor = 0
    for voto in lista_votos:
        if voto:
            votos_favor  = votos_favor + 1
        if votos_favor >= mayoria_absoluta:
            return True
        
    return False
                           
#%%
def calcular_aprobados(lista_notas):
    cantidad_aprobados = 0
    for nota in lista_notas: # es el recorrido de la lista
        if nota >= 3.0:
            cantidad_aprobados  = cantidad_aprobados + 1
            return cantidad_aprobados
 
        
       