# Infraestructura
attempts: list[str] = ["ana", "pedro", "juan", "ana", "luis", "ana", "admin"]

blocked: list[str] = ["pedro", "luis"]


# Dominio
def clasificar(users):
    listValido: list[str] = []
    listBloqueados: list[str] = []

    for usuario in users:
        if usuario in blocked and usuario not in listBloqueados:
            listBloqueados.append(usuario)
        elif usuario not in blocked and usuario not in listValido:
            listValido.append(usuario)

    return listValido, listBloqueados


listoV, listoB = clasificar(attempts)

# Servicios
print(f"Intentos válidos: {len(listoV)}")
print(f"Intentos bloqueados: {len(listoB)}")
print(f"Usuarios válidos únicos:  {listoV}")
print(f"Usuarios bloqueados únicos: {listoB}")
