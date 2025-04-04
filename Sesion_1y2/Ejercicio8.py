#Variables y constantes
dolares = int(input("Ingrese la cantidad de dolares a convertir: "))
EURO = 0.9
LIBRA = 0.76
YEN = 145.67

#Calculos
euros = dolares * EURO
libras = dolares * LIBRA
yenes = dolares * YEN

#Resultado
print("-"*100)
print(f'${dolares} dolares equivalen a €{euros: .2f} euros, £{libras: .2f} libras esterlinas y ¥{yenes: .2f} yenes')