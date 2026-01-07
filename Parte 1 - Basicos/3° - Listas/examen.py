"""
Crea una lista llamada cities con al menos 5 ciudades.
Luego:
- Agrega una ciudad al final
- Inserta una ciudad en la posición 1
- Elimina una ciudad usando pop()
- Elimina otra usando remove()
- Imprime la lista final
"""

cities: list[str] = ["Uruapan", "Morelia", "Zamora", "Paztcuaro", "Cardenas"]

cities.append("Paracho")

print(cities)

cities.insert(1, "Zihuatanejo")

print(cities)

descalificada = cities.pop(3)

print(f"la ciudad descalificada fue {descalificada}")

cities.remove("Cardenas")

print(cities)

"""
Tienes esta lista:

numbers = [3, 1, 4, 2, 5]

Escribe código para:
- Imprimir la lista ordenada temporalmente
- Imprimir la lista original
- Ordenar la lista permanentemente
- Invertir el orden de la lista

"""

numbers: list[int] = [3, 1, 4, 2, 5]

print(sorted(numbers))

print(numbers)

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)


"""
    Dada esta lista:

animals = ['perro', 'gato', 'conejo', 'loro', 'pez']


Escribe código que imprima:
- El primer animal
- El último animal
- Los primeros 3 animales
- El tamaño de la lista

"""

animals: list[str] = ["perro", "gato", "conejo", "loro", "pez"]

print(animals[0])

print(animals[-1])

print(animals[0:3])

print(len(animals))
