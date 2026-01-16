def saludar():
    print("Hola!")


def despedir():
    print("Adiós!")


acciones = {
    "1": saludar,
    "2": despedir,
}

opcion = input("Elige 1 o 2: ")

accion = acciones.get(opcion)

if accion:
    accion()
else:
    print("Opción inválida")
