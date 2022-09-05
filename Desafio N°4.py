# -*- coding: utf-8 -*-
#Desafío 4:
#Realizar un programa en el cual se ingresen dos números e informe si el primero es múltiplo del segundo.
#En caso contrario deberá generar un mensaje adecuado.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero2 % numero1 == 0:
    print("El primer numero ES multiplo del segundo numero...")
else:
    print("El primer numero NO ES multiplo del segundo numero...")