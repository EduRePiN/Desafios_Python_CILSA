#Desafío 16:
#Crear un diccionario con los siguientes pares de clave - valor:
#Ejemplo:
#{
#"nombre": "Eduardo",
#"edad": 27,
#"correo": "eduardo78d@gmail.com",
#"cursos": ["Python", "MongoDB", "Flask"]
#}

#Completar los valores del diccionario con tus datos personales.
#Convertirlo al formato JSON y mostrar los datos por consola.

import json

miDiccionario = {
    "nombre": "Eduardo",
    "edad": 35,
    "correo": "edurepin@gmail.com",
    "cursos": ["JavaScript", "Python", "Html", "Css"]
}

convertirDatos = json.dumps(miDiccionario)

print(convertirDatos)