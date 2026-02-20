def multiplicar(*num):
    resultado = 1
    for x in num:
        resultado *= x

    return resultado


print(multiplicar(1, 2, 3))


diccionario = {
    "Nombre": "Laura",
    "Edad": 30,
    "Ciudad": "Lima",
}


def describir_persona(**info):
    nombre = info.get("Nombre", "Desconocido")
    edad = info.get("Edad", "No especificada")
    ciudad = info.get("Ciudad", "No especificada")

    return nombre, edad, ciudad


nombre, edad, ciudad = describir_persona(**diccionario)

print(f"Bienvenido {nombre} de edad {edad} de la ciudad {ciudad}")
