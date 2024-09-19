###calcular cómo se desempeñaría un jugador durante un juego completo de 48
### minutos basándose en su rendimiento actual
def nba_extrap(ppg, mpg):
    # Si minutos por juego es 0, retorna 0
    if mpg == 0:
        return 0
    # Extrapolación de puntos por juego a 48 minutos
    extrapolated_ppg = (ppg * 48) / mpg
    # Redondear al décimo más cercano
    return round(extrapolated_ppg, 1)

# Ejemplos de uso
print(nba_extrap(12, 20))  # 28.8
print(nba_extrap(10, 10))  # 48.0
print(nba_extrap(5, 17))   # 14.1
print(nba_extrap(0, 0))    # 0
