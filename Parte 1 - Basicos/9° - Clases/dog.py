class Perro:
    """
    Un simple intento de un modelo de perro
    """

    def __init__(self, name, age):
        """
        Inicializa atributos
        """
        self.name = name

        self.age = age

    def sit(self):
        """
        Simula al perro sentandose por un comando
        """
        print(f"{self.name} esta ahora sentad@")

    def roll_over(self):
        """
        Simula al perro dando una voltereta
        """
        print(f"{self.name} acaba de dar una vuelta")


miPerro = Perro("Siquito", 10)

print(f"Mi perro se llama {miPerro.name}")
print(f"Su edad es de {miPerro.age}")

miPerro.sit()
miPerro.roll_over()
