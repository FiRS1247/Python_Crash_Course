# ¿Por qué with? Garantiza que el archivo se cierra aunque ocurra una excepción.
# Es el estándar — nunca uses open() sin with en código serio.

# Escribir un archivo
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Segunda línea\n")
# Leer un archivo completo
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea (eficiente en memoria — importante para archivos grandes)
with open("datos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# Append — agregar sin borrar
with open("datos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Línea nueva\n")

# Para lectura y escritura se usar el parametro "r+"
