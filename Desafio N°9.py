# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:16:12 2022

@author: Eduardo
"""

#Desafío 9:
#Implementar control de excepciones a partir del programa desarrollado en el desafío anterior (desafío 8)

numero_grande = -99999999999999

numero = int(input("Ingrese un numero, o el 0 (cero) para finalizar: "))

try:
    for i in range(99999999999999999):
        if numero > numero_grande:
            numero_grande = numero
        numero = int(input("Ingrese un numero, o el 0 (cero) para finalizar: "))
        if numero == 0:
            break
except:
    print("Ingreso un numero no valido")
    

print("El numero mas grande ingresado fue:", numero_grande)