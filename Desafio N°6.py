# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 20:36:53 2022

@author: Eduardo
"""

#Desafío 6:
#Realizar un programa donde se ingresen 5 números e informe el promedio de los números ingresados.
#Nota: utilizar estructuras repetitivas

print("Ingrese 5 numeros")

promedio = 0
numeros = 0
suma = 0

for numeros in range(0,5):
    numeros = int(input("Ingrese un numero: "))
    suma = suma + numeros
    promedio = float(suma / 5)
    
print("El promedio de los numeros ingresados es: ", promedio)