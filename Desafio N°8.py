# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:40:51 2022

@author: Eduardo
"""

#Desafío 8:
#Realizar el programa del desafío 7 pero implementarlo mediante la estructura For.

numero_grande = -99999999999999

numero = int(input("Ingrese un numero, o el 0 (cero) para finalizar: "))

for i in range(99999999999999999):
    if numero > numero_grande:
        numero_grande = numero
    numero = int(input("Ingrese un numero, o el 0 (cero) para finalizar: "))
    if numero == 0:
        break
print("El numero mas grande ingresado fue:", numero_grande)