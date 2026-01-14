# Infraestructura
user = "juan"
role = "cliente"
age = 22
cart_total = 1200
coupon = "DESC10"
banned_users: list[str] = ["pedro", "luis"]


# Dominio
def is_banned(user):
    return user in banned_users


def is_adult(age):
    return age >= 18


def get_access(role, age):
    if role == "admin":
        return "Acceso completo"
    elif role == "cliente" and is_adult(age):
        return "Acceso normal"
    elif role == "cliente" and not is_adult(age):
        return "Acceso limitado"
    else:
        return "Solo lectura"


def calculate_discount(cart_total, coupon, role):
    if cart_total > 2000 or role == "admin":
        return 0.20
    elif cart_total > 1000 and coupon == "DESC10":
        return 0.10
    else:
        return 0


def calculate_total(cart_total, discount):
    return cart_total * (1 - discount)


# Servicios
print("Iniciando sistema")

if is_banned(user):
    print(f"Usuario {user} bloqueado")
else:
    access = get_access(role, age)
    discount = calculate_discount(cart_total, coupon, role)
    total = calculate_total(cart_total, discount)

    print(f"Acceso: {access}")
    print(f"Descuento: {int(discount * 100)}%")
    print(f"Total: {total}")
