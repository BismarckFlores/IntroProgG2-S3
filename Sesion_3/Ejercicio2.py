#Leer x cantidad de producto comprado a x precio
#Aplica un IVA del 15%
#Un descuentno del 10%
#Mostrar el total antes del IVA
#Monto del IVA
#Monto del descuento
#Total a pagar
""" Se debe leer el nombre del cliente, nombre del producto y mostrar
una factura """

print("="*22)
print("Sistema de facturación")
print("="*22)
print("Ingrese los siguientes datos")
cliente = input("Nombre del cliente: ")
producto = input("Nombre del profucto: ")
precio = float(input("Precio del producto: "))
cantidad = float(input("Cantidad del producto: "))

total = precio * cantidad
iva = total * 0.15
descuento = total * 0.1
monto = total + iva - descuento

import os

pressKey = input("Precion una tecla para continuar...")

os.system("cls || clear")

print("+"*30)
print("Factura")
print("+"*30)
print(f'Cliente: {cliente}')
print("Productos \t Cantidad \t Precio \t Total")
print (f"{producto:<10} {cantidad:<10} {precio:<10} {total:<10}")
print(f'IVA: {iva}')
print(f'Desc: {descuento}')
print(f'Monto: {monto}')