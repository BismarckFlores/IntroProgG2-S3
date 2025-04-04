#Variables
salarioBruto = float(input("Porfavor ingrese su salario bruto: "))
impuestoRenta = salarioBruto * 0.1
seguroSocial = salarioBruto * 0.05
fondosPension = salarioBruto * 0.03

#Calculos
descuentoSalarial = impuestoRenta + seguroSocial + fondosPension
salarioNeto = salarioBruto - descuentoSalarial

#resultados
print("-"*100)
print(f'Tu salario bruto es de {salarioBruto: .2f} y de este se te descuentan {descuentoSalarial: .2f} de este')
print(f'Tu salario neto es de {salarioNeto}')