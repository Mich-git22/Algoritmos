##Calcular la presión total en un recipiente con dos tipos de moléculas
def calculate_pressure(M1, M2, m1, m2, V, T):
    # Convertir temperatura a Kelvin
    T_kelvin = T + 273.15

    # Constante de los gases en dm³·atm·K⁻¹·mol⁻¹
    R = 0.082

    # Calcular el número de moles de cada molécula
    n1 = m1 / M1
    n2 = m2 / M2

    # Calcular la presión total usando la fórmula
    P_total = (n1 + n2) * R * T_kelvin / V

    return P_total


# Ejemplo de uso
M1 = 28.0  # Masa molar de la primera molécula en g/mol
M2 = 44.0  # Masa molar de la segunda molécula en g/mol
m1 = 10.0  # Masa presente de la primera molécula en gramos
m2 = 20.0  # Masa presente de la segunda molécula en gramos
V = 5.0  # Volumen del recipiente en dm³
T = 25.0  # Temperatura en °C

# Calcular la presión total
pressure = calculate_pressure(M1, M2, m1, m2, V, T)
print(f'La presión total es {pressure:.2f} atm')
