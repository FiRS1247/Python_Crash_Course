# Ejercicio 1 — Lista dentro de diccionario
# Infraestructura
cursos: dict[str, list[str]] = {
    "Python": ["Juan", "Ana", "Pedro"],
    "Django": ["Luis", "Ana"],
}


# Dominio
def nomCurso(cursos):
    listpy = []
    listdj = []

    for curso, alumnos in cursos.items():
        if curso == "Python":
            listpy = alumnos
        elif curso == "Django":
            listdj = alumnos

    return listpy, listdj


def agregarEst(clase, usuario):
    cursos[clase].append(usuario)


# Servicios
listA, listB = nomCurso(cursos)
print(f"Los estudiantes de Python son {listA}")
print(f"Los estudiantes de Django son {listB}")

agregarEst("Django", "Leon")
print("Integramos un nuevo alumno")

listA, listB = nomCurso(cursos)
print(f"Los estudiantes de Python son {listA}")
print(f"Los estudiantes de Django son {listB}")


print("---------------------------------------------------------------")

# Ejercicio 2 — Diccionario dentro de lista
# Infraestructura

usuarios: list[dict[str, str | int]] = [
    {"nombre": "Juan", "edad": 22, "rol": "cliente"},
    {"nombre": "Ana", "edad": 25, "rol": "admin"},
    {"nombre": "Pedro", "edad": 17, "rol": "invitado"},
]


# Dominio
def procesar_usuarios(usuarios):
    nombre_roles = []
    admins = []
    mayores = 0

    for u in usuarios:
        nombre_roles.append((u["nombre"], u["rol"]))

        if u["edad"] >= 18:
            mayores += 1

        if u["rol"] == "admin":
            admins.append(u["nombre"])

    return nombre_roles, mayores, admins


# Servicios
nombre_roles, mayores, admins = procesar_usuarios(usuarios)

for nombre, rol in nombre_roles:
    print(f"{nombre} - {rol}")

print(f"Usuarios mayores de edad: {mayores}")
print(f"Admins: {admins}")

print("---------------------------------------------------------")
# Ejercicio 3 Procesar productos
# Infraestructura
productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 100},
    {"nombre": "Monitor", "precio": 300, "stock": 0},
]

# Dominio


def clasificar_producto(lista):
    producto_precio = []
    stock = 0
    agotados = []

    for producto in lista:
        producto_precio.append((producto["nombre"], producto["precio"]))

        if producto["stock"] > 0:
            stock += producto["stock"]
        else:
            agotados.append(producto["nombre"])

    return producto_precio, stock, agotados


# Servicios

producto_precio, stock, agotados = clasificar_producto(productos)

for nombre, precio in producto_precio:
    print(f"El producto {nombre} y cuesta {precio}")

print(f"El stock total es {stock}")

for nombre in agotados:
    print(f"El producto {nombre} esta agotado")
