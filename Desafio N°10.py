# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:28:31 2022

@author: Eduardo
"""

#Desafío 10:
#Cargar un conjunto de notas utilizando una lista
#Mostrar las notas cargadas en la lista.

notas_lista = []

q_notas = int(input("Ingrese la cantidad de notas a cargar: "))

for i in range(q_notas):
    notas = int(input("Ingrese la nota del alumno: "))
    if notas >= 0 and notas <= 10:
        notas = notas_lista.append(notas)

print(notas_lista)