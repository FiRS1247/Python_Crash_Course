# 3.4 lista de clientes

clientes: list[str] = ["Jose", "Maria", "Juan", "Paco"]


print(f"hola {clientes[0:]}, los quiero invitar a una cena muy especial")

# 3.5 Modificar lista

clientes[1] = "Josue"

print(f"hola {clientes[0:]}, los quiero invitar a una cena muy especial")

# 3.6 Agregar mas elementos a la lista

clientes.insert(0, "Leo")

clientes.insert(3, "Gabriel")

clientes.append("Brayan")

print(f"hola {clientes[0:]}, los quiero invitar a una cena muy especial")

# 3.7 Eliminando elementos

borrado = clientes.pop(3)

print(f"Lo siento {borrado}, pero no puedes venir")

del clientes[0:2]

print(f"hola {clientes[0:]}, los quiero invitar a una cena muy especial")


# 3.8 Acomodando la lista


print(sorted(clientes))

clientes: list[str] = ["Jose", "Maria", "Juan", "Paco"]

clientes.sort()

print(clientes)
