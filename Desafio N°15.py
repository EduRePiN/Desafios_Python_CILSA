# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:47:29 2022

@author: Eduardo
"""

#Desafío 15:
#Utilizar Excel o Google spreadsheets
#Generar un archivo con los siguientes campos:
#Nombre, Apellido, Edad, Barrio
#Cargar algunas líneas y exportarlo como CSV
#Realizar un programa que me permita mostrar el contenido del archivo

contenido = open("Desafio N°15.csv", "r")

contador = 1

for celda in contenido:
    print(contador, ":", celda)
    contador = contador + 1
contenido.close()