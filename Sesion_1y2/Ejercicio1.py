tempFah = float(input("Ingresa la temperatura en F°: "))

# tempCel = tempFah - 32
# tempCel = tempCel * 5
# tempCel = tempCel / 9

tempCel = ((tempFah - 32) * 5) / 9

TempKelv = tempCel + 273.15

print(f'Grados Celcius: {tempCel: .2f}')
print(f'Grados Kelvin: {TempKelv: .2f}')