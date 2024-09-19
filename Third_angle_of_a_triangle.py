##CALCULA LA SUMA DE ANGULOS DE UN TRIANGULO
def third_angle(angle1, angle2):
    # La suma de los ángulos de un triángulo es siempre 180 grados
    return 180 - (angle1 + angle2)

# Ejemplo de uso
print(third_angle(60, 80))  # Devuelve 40
print(third_angle(45, 45))  # Devuelve 90
