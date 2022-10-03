# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:29:54 2022

@author: Eduardo
"""

#Desafío 13:
#Desarrollar una función que realice la división de dos números, en caso de ser posible devuelve el resultado.
#La función debe contemplar el tratamiento de excepciones.
#Probar la función.



def division():
    try:
        numero1 = int(input("Ingrese el dividendo: "))
        numero2 = int(input("Ingrese el divisor: "))
        resultado = numero1/numero2
        print("La division da como resultado: ", resultado)
    except ZeroDivisionError:
        print("No se puede divir por cero!")
    except ValueError:
        print("No se puede dividir letras")
        
division()
    