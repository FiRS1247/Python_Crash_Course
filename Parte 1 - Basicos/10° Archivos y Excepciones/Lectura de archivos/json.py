import json

# Guardar datos estructurados
usuario = {
    "nombre": "Fernando",
    "rol": "admin",
    "permisos": ["read", "write", "delete"],
}

with open("usuario.json", "w", encoding="utf-8") as f:
    json.dump(usuario, f, indent=4, ensure_ascii=False)

# Leer JSON
with open("usuario.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

print(datos["nombre"])  # Fernando
