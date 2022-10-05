# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:18:03 2022

@author: Eduardo
"""

#Desafío 14:
#Realizar un programa que cargue 5 personas con sus datos, nombre, apellido y edad.
#Se debe almacenar en un diccionario y luego escribir un archivo separado por comas con los datos de cada registro del diccionario.

persona = {
    "nombre" : [],
    "apellido" : [],
    "edad" : [],
    }

for i in range(5):
    nombre = input("Ingrese el nombre: ")
    persona["nombre"].append(nombre)
    apellido = input("Ingrese el apellido: ")
    persona["apellido"].append(apellido)
    edad = input("Ingrese la edad: ")
    persona["edad"].append(edad)


contenido = open("personas.txt", "w")

for i in range(5):
    contenido.write(persona["nombre"] [i] + " , ")
    contenido.write(persona["apellido"] [i] + " , ")
    contenido.write(persona["edad"] [i] + "\n")

contenido.close()
