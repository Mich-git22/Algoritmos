def usdcny(usd):
    # Convertir USD a CNY
    cny = usd * 6.75
    # Formatear el resultado a 2 decimales y devolver como cadena
    return f"{cny:.2f} Chinese Yuan"

# Solicitar al usuario la cantidad de USD a convertir
usd_input = float(input("Ingresa la cantidad de USD que deseas convertir: "))

# Llamar a la función y mostrar el resultado
result = usdcny(usd_input)
print(result)
