suma = 0

while True:
    ingreso = input("Agrega un numero para la suma")
    if ingreso == "exit":
        break
    else:
        suma += int(ingreso)
        print(f"Agregaste el numero {ingreso}")

print(f"La suma fue de {suma}")
