# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:30:28 2022

@author: Eduardo
"""

#Desafío 7:
#Realizar un programa en el cual se ingresen números enteros y se obtenga el mayor de ellos.
#Se desconoce cuantos números serán ingresados pero se sabe que cuando se ingrese el valor 0,
#el programa finalizará indicando el máximo número cargado.

numero_grande = -99999999999999
numero = int(input("Ingrese un numero: "))

while numero != 0:
    if numero > numero_grande:
        numero_grande = numero
    numero = int(input("Ingrese otro numero o el 0 (cero) para finalizar: "))
    
print("El numero mas alto ingresado fue: ", numero_grande)