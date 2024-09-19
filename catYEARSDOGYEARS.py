def animal_years(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso:
print(animal_years(1))  # [1, 15, 15]
print(animal_years(2))  # [2, 24, 24]
print(animal_years(10))  # [10, 56, 64]