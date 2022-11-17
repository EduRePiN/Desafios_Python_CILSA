'''Dado el archivo "RecursosPython.xlsx"
1.Exportar el archivo a csv.
2.Crear un diccionario que permita almacenar la información del archivo convertido.
3.Realizar un filtro que permita visualizar los datos de las personas cuyo apellido es "Gómez".
4.Generar un archivo csv que permita guardar los datos de las personas que viven en "Córdoba" o en "Santa Fe".'''

contenido = open("recursosPython.csv", "r")
diccionario = []
contador = int(0)

for linea in contenido:
    x = linea.split(";")
    dni = x[0]
    nombre = x[1]
    apellido = x[2]
    email = x[3]
    fechaDeNacimiento = x[4]
    lugarDeResidencia = x[5]

    if apellido == "Gomez":
        print("DNI: ", dni, " Nombre: ", nombre, " Apellido: ", apellido, " Email: ", email, " Fecha de nacimiento: ",
              fechaDeNacimiento, "Lugar de Residencia: ", lugarDeResidencia)
        contador = contador + 1
    diccionario.append({"DNI": dni,
                        "Nombre": nombre,
                        "Apellido": apellido,
                        "Email": email,
                        "Fecha de nacimiento": fechaDeNacimiento,
                        "Lugar de residencia": lugarDeResidencia})
    pass

archivo = open("personas.txt", "w")
for linea in diccionario:
    dni = linea["DNI"]
    nombre = linea["Nombre"]
    apellido = linea["Apellido"]
    email = linea["Email"]
    fechaDeNacimiento = linea["Fecha de nacimiento"]
    lugarDeResidencia = linea["Lugar de residencia"]
    residencia = dni + "; " + nombre + "; " + apellido + "; " + email + "; " + fechaDeNacimiento + "; " + lugarDeResidencia
    if lugarDeResidencia == "Santa Fe\n" or lugarDeResidencia == "Cordoba\n":
        archivo.write(residencia)
    pass

archivo.close()