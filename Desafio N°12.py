# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:59:30 2022

@author: Eduardo
"""

#Desafío 12:
#Desarrollar una función que reciba el nombre de una persona y un valor entero.
#Si el valor entero es 0, imprimirá: "hola" y el nombre.
#Si el valor entero es distinto de 0 , imprimirá: "chau" y el nombre.
#Probar la función.

nombre = input("Escriba un nombre: ")
valor = int(input("Escriba un numero entero: "))

def nombreValor(): 
    if valor == 0:
        print("Hola", nombre)
    else:
        print("Chau", nombre)

nombreValor()