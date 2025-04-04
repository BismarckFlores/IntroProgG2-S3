#Calculos
viaje = sum([
    float(input("¿Cuántas horas dura tu primer vuelo?: ")),
    float(input("¿Cuántas horas dura tu primera escala?: ")),
    float(input("¿Cuántas horas dura tu segundo vuelo?: ")),
    float(input("¿Cuántas horas dura tu segunda escala?: ")),
    float(input("¿Cuántas horas dura tu tercer vuelo?: "))
])

#Resultados
print("-"*100)
print(f'El tiempo total del viaje es de {viaje} horas')