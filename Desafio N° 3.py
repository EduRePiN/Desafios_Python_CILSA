# -*- coding: utf-8 -*-
#Desafío 3:
#Realizar un programa en el cual se ingrese un numero entero e informe si es par.
#En caso que no sea par también deberá informar al respecto.

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero ingresado es par...")
else:
    print("El numero ingresado es impar...")