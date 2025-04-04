#Variables
precio = float(input("Digite el precio del producto: "))
porcentajeDescuento = int(input("Ingrese el valor del descuento a aplicar: "))
iva = int(input("Ingrese el porcentaje de IVA a aplicar: "))

#Calculos
descuento = (precio * porcentajeDescuento) / 100
precioDescuento = precio - descuento
precioIva = precioDescuento * iva
precioIva /= 100
precioFinal = precioDescuento + precioIva

#Resultados
print("-"*100)
print(f'El precio original es {precio} y el descuento aplicado es del {porcentajeDescuento}%')
print(f'El precio con el descuento es de {precioDescuento} y a eso se le aplica un IVA del {iva}%: {precioIva}')
print(f'El precio final del producto es de {precioFinal}')