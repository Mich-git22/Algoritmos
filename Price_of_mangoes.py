def mango(quantity, price):
    # Calcular cuántos mangos se obtienen gratis
    free_mango_groups = quantity // 3
    # Calcular la cantidad de mangos que se deben pagar
    paid_mangos = quantity - free_mango_groups
    # Calcular el costo total
    total_cost = paid_mangos * price
    return total_cost

# Ejemplos de uso
print(mango(2, 3))  # Debería imprimir 6
print(mango(3, 3))  # Debería imprimir 6
print(mango(5, 3))  # Debería imprimir 12
print(mango(9, 5))  # Debería imprimir 30
