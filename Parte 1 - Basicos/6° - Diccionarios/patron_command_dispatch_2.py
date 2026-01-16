def fecha():
    print("la fecha de hoy es 15/01/2026")


def nombre():
    print("El nombre es Joe Doue")


acciones = {"1": fecha, "2": nombre}

opcion = input("Escoge 1 o 2")

accion = acciones.get(opcion)

if accion:
    accion()
else:
    print("Eso no era una opcion")
