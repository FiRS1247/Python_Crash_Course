# Infraestructura
orders: list[int] = [1200, 300, 4500, 50, 1800, 700]


# Dominio
def recoLista(orders):
    ignorados: list[int] = []
    normales: list[int] = []
    premium: list[int] = []

    for order in orders:
        if order < 100:
            ignorados.append(order)
        elif 100 <= order <= 1000:
            normales.append(order)
        else:
            premium.append(order)

    return ignorados, normales, premium


def obtenerTotal(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


listPi, listPN, listPP = recoLista(orders)

# Servicios
print(f"- Pedidos ignorados: {len(listPi)} con total {obtenerTotal(listPi)}")
print(f"- Pedidos normales: {len(listPN)} con total {obtenerTotal(listPN)}")
print(f"- Pedidos premium: {len(listPP)} con total {obtenerTotal(listPP)}")
