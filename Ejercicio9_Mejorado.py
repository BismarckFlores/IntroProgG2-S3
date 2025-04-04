#Variables
duración = float(input("Ingrese la duración de la pelicula en minutos: "))
comercialesPrevios = float(input("Ingrese la duración de los comerciales previos: "))
cantidadPausas = int(input("Ingrese la cantidad de pausas comerciales durante la pelicula: "))

#Duración de cada pausa
pausas = []
for i in range(cantidadPausas):
    pausa = float(input(f'Ingrese la duracion de la pausa {i+1}: '))
    pausas.append(pausa)
    
#calculos
totalComerciales = sum(pausas) + comercialesPrevios
duraciónTotal = duración + totalComerciales

print("-"*100)
print(f'La duracion original de la pelicula es de {duración} minutos')
print(f'La duracion total de los comerciales fue de {totalComerciales} minutos')
print(f'El tiempo total de proyección fue de {duraciónTotal} minutos')