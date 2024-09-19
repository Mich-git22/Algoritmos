def format_number(num):
    # Redondear el número a dos decimales
    rounded_num = round(num, 2)
    # Convertir el número redondeado a una cadena con formato de dos decimales
    formatted_num = f"{rounded_num:.2f}"
    return formatted_num

# Ejemplos de uso
print(format_number(5.5589))  # Output: '5.56'
print(format_number(3.3424))  # Output: '3.34'
print(format_number(10))      # Output: '10.00'
print(format_number(7.1))     # Output: '7.10'
