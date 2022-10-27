#Desafío 17:

#Implementar una clase Calculadora que defina los métodos:
#Sumar, Restar, Multiplicar y Dividir. En lo posible realice tratamiento de excepciones.
#Probar la clase Calculadora.

class calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(numero1, numero2):
        print("El resultado de la suma es: ", float(numero1 + numero2))

    def restar(numero1, numero2):
        print("El resultado de la resta es: ", float(numero1 - numero2))

    def multiplicar(numero1, numero2):
        print("El resultado de la multiplicacion es: ", float(numero1 * numero2))

    def dividir(numero1, numero2):
        try:
            print("El resultado de la division es: ", float(numero1 / numero2))
        except ZeroDivisionError:
            print("No se puede dividir un numero por 0")

try:
    suma1 = float(input("Ingrese el 1er numero para sumar: "))
    suma2 = float(input("Ingrese el 2do numero para sumar: "))
    calculadora.sumar(suma1, suma2)
    restar1 = float(input("Ingrese el 1er numero para restar: "))
    restar2 = float(input("Ingrese el 2do numero para restar: "))
    calculadora.restar(restar1, restar2)
    multiplico1 = float(input("Ingrese el 1er numero para multiplicar: "))
    multiplico2 = float(input("Ingrese el 2do numero para multiplicar: "))
    calculadora.multiplicar(multiplico1, multiplico2)
    divido1 = float(input("Ingrese el 1er numero para dividir: "))
    divido2 = float(input("Ingrese el 2do numero para dividir:"))
    calculadora.dividir(divido1, divido2)
except:
    print("Ocurrio un error")
