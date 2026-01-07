# 2.3 Mensaje personalizado

# nombre = input("Por favor, ingresa tu nombre: ")
nombre = "fernando ivan rocha salgado"

print(f"Hola, {nombre} quieres aprender algo de python en dia de hoy?")

print("----------------------------------------------------------------")
# 2.4 Nombre con diferentes formatos

print(nombre.upper())

print(nombre.lower())

print(nombre.title())

print(nombre.capitalize())

print("----------------------------------------------------------------")

# 2.5 y 2.6 Nota famosa

personaje = "Marco Aurelio"
Mensaje = "No te estreses por lo que no puedes controlar"

print(f"{personaje} una vez dijo,\n '{Mensaje}'")

print("----------------------------------------------------------------")

# 2.7 saltos de linea

print(
    f"Hola {nombre.title}, \n espero que estes disfrutando aprendiendo python, solo recuerda: \n\t - usar siempre ruff \n\t - usar siempre sonalint \n\t - usar siempre prospector"
)

print("----------------------------------------------------------------")

# Extension de archivo

archivo = "escritorio/chamin.py"

print(archivo.removeprefix("escritorio/"))

print(archivo.removesuffix(".py"))

print(archivo.removesuffix(".py").removeprefix("escritorio/"))

print("----------------------------------------------------------------")
