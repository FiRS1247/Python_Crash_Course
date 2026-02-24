from car import Car, carro_electrico

mi_nuevo_carro = Car("Chevrolet", "Corsa", 2004)
print(mi_nuevo_carro.obtener_descripcion())

mi_nuevo_carro_electrico = carro_electrico("BYD", "King", 2025)
print(mi_nuevo_carro_electrico.tamaño_bateria())
print(mi_nuevo_carro_electrico.obtener_descripcion())
