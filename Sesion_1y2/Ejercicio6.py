#Variables
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

#Calculos
imc = peso / (altura ** 2)
clasificación = imc * 100
clasificación /= 100
clasificación = round(clasificación, 2)
imc = round(imc, 2)

# Clasificación del IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 24.9:
    clasificacion = "Normal"
elif imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

#Resultados
print("-"*100)
print(f'Tu peso es de {peso} Kg')
print(f'Tu altura es de {altura} metros')
print(f'Tu valor de IMC es de {imc}')
print(f'Tu clasificación del IMC según los valores estándar es: {clasificacion}')
