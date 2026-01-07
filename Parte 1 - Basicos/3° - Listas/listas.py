# Esto es una lista en python

marcas_de_celulares: list[str] = ["Samsung", "Apple", "Xiaomi", "Huawei"]
print("Marca mas popular: " + marcas_de_celulares[0])

# Ejercicio 3.1 Nombres
# Guarda los nombres de algunas personas en una lista y luego imprime cada nombre individualmente.
amigos: list[str] = ["Carlos", "Leo", "Francisco"]
print("Amigo 1: " + amigos[0])
print("Amigo 2: " + amigos[1])
print("Amigo 3: " + amigos[2])


# Ejercicio 3.2 Saludos
# Usa la lista del ejercicio anterior para imprimir un saludo personalizado para cada persona.
print("Hola " + amigos[0] + ", ¿cómo estás?")

# 3.3 Tu propia lista

transportes: list[str] = ["motoclicleta", "carro", "autobus"]

print(
    f"Me gustaria tener una {transportes[0]} ,pero tengo un {transportes[1]} ,aunque no me molesta tomar el {transportes[2]} por que es mas ecologico y barato si es que pudiera pagarlo con tarjeta de credito"
)
