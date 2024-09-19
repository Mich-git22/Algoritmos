import math


def age_range(age):
    if age > 14:
        # Usar la regla clásica para edades mayores a 14
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Usar la fórmula simplificada para edades menores o iguales a 14
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplos de uso
print(age_range(27))  # Output: 20-40
print(age_range(5))  # Output: 4-5
print(age_range(17))  # Output: 15-20
