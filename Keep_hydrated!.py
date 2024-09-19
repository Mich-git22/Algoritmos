import math

def litres(time):
    # Calcula el número de litros y redondea hacia abajo
    return math.floor(time * 0.5)

# Ejemplos de uso
print(litres(3))    # Devuelve 1
print(litres(6.7))  # Devuelve 3
print(litres(11.8)) # Devuelve 5
