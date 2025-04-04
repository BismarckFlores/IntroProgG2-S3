#Variables
duración = float(input("Ingrese la duración de la pelicula en minutos: "))
comercialesPrevios = float(input("Ingrese la duración de los comerciales previos: "))
cantidadPausas = int(input("Ingrese la cantidad de pausas comerciales durante la pelicula: "))
duracionPausa = float(input("4. Ingrese la duración de cada pausa comercial: "))

#Calculos
totalComercialesDurante = cantidadPausas * duracionPausa
peliculaPrevios = duración + comercialesPrevios
duraciónTotal = peliculaPrevios + totalComercialesDurante

print("-" * 100)
print(f"Duración original de la película: {duración} minutos")
print(f"Duración total de los comerciales: {comercialesPrevios + totalComercialesDurante} minutos")
print(f"Tiempo total de la proyección: {duraciónTotal} minutos")