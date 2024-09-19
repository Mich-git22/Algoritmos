def convertir_resolucion(x, y):
    # Relación de aspecto 16:9
    nuevo_ancho = round(y * 16 / 9)

    return nuevo_ancho, y


# Ejemplo de uso:
x_original, y_original = 374, 280
nuevo_x, nuevo_y = convertir_resolucion(x_original, y_original)
print(f"Resolución original: {x_original}x{y_original}")
print(f"Nueva resolución con relación 16:9: {nuevo_x}x{nuevo_y}")
