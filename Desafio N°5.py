# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 20:16:17 2022

@author: Eduardo
"""

#"Desafío 5:
#"Realizar un programar en el cual se ingrese:
#"1) el limite inferior de un intervalo
#"2) el limite superior del mismo intervalo
#"3) Un valor entero
#"Indicar si el valor entero ingresado en el punto 3 se encuentra dentro del intervalo definido por los valores del punto (1) y del punto (2).

linferior = int(input("Ingrese el limite inferior:"))
lsuperior = int(input("Ingrese el limete superior:"))
numero = int(input("Ingrese un numero:"))

if numero >= linferior and numero <= lsuperior:
    print("El numero ingresado se encuentra en el intervalo entre", linferior, "y", lsuperior)
else:
    print("El numero ingresado NO se encuentra en el intervalo entre", linferior, "y", lsuperior)