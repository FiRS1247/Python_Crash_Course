# Contar hacia 20
maximo = 20
conteo: list[int] = list(range(1, (maximo + 1)))

for numero in conteo:
    print(numero)

# Contar hacia un millon

dinero: list[int] = list(range(1, 1000000 + 1))

for indice in dinero:
    print(indice)
    break

print(min(dinero))

print(max(dinero))

print(sum(dinero))


impares: list[int] = list(range(1, 20 + 1, 2))

for valor in impares:
    print(valor)
