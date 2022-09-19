# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:20:26 2022

@author: Eduardo
"""

#Desafío 11:
#Retomar el ejercicio del desafío anterior pero solo cargar en la lista aquellas notas
#que estén entre  6 y 10 (inclusive)
#Mostrar las notas cargadas en la lista.


notas_lista = []

q_notas = int(input("Ingrese la cantidad de notas a cargar: "))

for i in range(q_notas):
    notas = int(input("Ingrese la nota del alumno: "))
    if notas >= 6 and notas <= 10:
        notas = notas_lista.append(notas)

print(notas_lista)