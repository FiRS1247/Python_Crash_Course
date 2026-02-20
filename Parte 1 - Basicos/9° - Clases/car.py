class Car:
    """_summary_

    Args:
        fabricante (_type_): _description_
        modelo (_type_): _description_
        año (_type_): _description_
    """

    def __init__(self, fabricante, modelo, ano):

        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.lectura_odometro = 0

    def obtener_descripcion(self):

        nombre_completo = f"{self.ano} {self.fabricante} {self.modelo}"
        return nombre_completo.title()

    def leer_odometro(self):
        print(f"Este carro tiene un valor de {self.lectura_odometro} en el odometro")

    def actualizar_odometro(self, km):
        if km >= self.lectura_odometro:
            self.lectura_odometro = km
        else:
            print("No deberia reducir el km de tu carro pillo")

    def incrementar_odometro(self, km):
        self.lectura_odometro += km


mi_nuevo_carro = Car("Chevrolet", "Corsa", 2004)

print(mi_nuevo_carro.obtener_descripcion())
mi_nuevo_carro.leer_odometro()

mi_nuevo_carro.actualizar_odometro(24)
mi_nuevo_carro.leer_odometro()

mi_nuevo_carro.incrementar_odometro(20)
mi_nuevo_carro.leer_odometro()


class carro_electrico(Car):
    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        self.tamaño_bateria_integrada = 40

    def tamaño_bateria(self):
        print(f"El tamaño de la bateria es de {self.tamaño_bateria_integrada}")


mi_nuevo_carro_electrico = carro_electrico("Toyota", "Camry", 2025)
print(mi_nuevo_carro_electrico.obtener_descripcion())
mi_nuevo_carro_electrico.tamaño_bateria()
