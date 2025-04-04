#Variables
vuelo1 = float(input("Cuantas horas dura tu primer vuelo: "))
escala1 = float(input("Cuantas horas dura tu vuelo: "))
vuelo2 = float(input("Cuantas horas dura tu segundo vuelo: "))
escala2 = float(input("Cuantas horas dura tu vuelo: "))
vuelo3 = float(input("Cuantas horas dura tu vuelo: "))

#Calculos
viaje = vuelo1 + escala2
viaje += vuelo2
viaje += escala2
viaje += vuelo3

#Resultados
print("-"*100)
print(f'El tiempo total del viaje es de {viaje} horas')