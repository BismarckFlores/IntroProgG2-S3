# Variables y constantes
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
PI = 3.141592

# Calculos
areaBase = PI * (radio ** 2)
volumen = areaBase * altura
areaLateral = 2 * PI * radio * altura
areaSuperficial = areaLateral + 2 * areaBase

#Resultados
print("-"*100)
print(f'El cilindro ingresado tiene un radio de {radio: .2f} y una altura de {altura: .2f}')
print(f'El volumen del cilindro es de {volumen: .2f}')
print(f'El área superficial del cilindro es de {areaSuperficial: .2f}')