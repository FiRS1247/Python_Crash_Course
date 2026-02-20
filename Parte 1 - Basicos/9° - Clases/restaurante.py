class Restaurante:
    def __init__(self, nombre, estilo):
        """
        _summary_

        Inicializa el objeto

        Args:
            nombre (String): _description_
            estilo (String): _description_
        """

        self.nombre = nombre
        self.estilo = estilo

    def restaurante_descripcion(self):
        """
        _summary_
        Da una descripcion del restaurante
        """
        print(f"El restaurante {self.nombre} es de cocina {self.estilo}")

    def esta_abrierto(self):
        """
        _summary_
        Indica si el restaurante esta abierto
        """
        print(f"El restaurante {self.nombre} esta abierto")


elRestaurante1 = Restaurante("Paty", "Tacos")
elRestaurante2 = Restaurante("Xong", "China")
elRestaurante3 = Restaurante("bibriesca", "Chamorro")

elRestaurante1.restaurante_descripcion()
elRestaurante2.restaurante_descripcion()
elRestaurante3.restaurante_descripcion()
