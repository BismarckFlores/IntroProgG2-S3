#Variable
totalSegundos = int(input("Porfavor ingrese la cantidad de segundos que desea convertir: "))

#Calculos
horas = totalSegundos // 3600
segundosUsadosHoras = horas * 3600
segundosRestantes = totalSegundos - segundosUsadosHoras
minutos = segundosRestantes // 60
segundosUsadosMinutos =  minutos * 60
segundosFinales = segundosRestantes - segundosUsadosMinutos

#Resultado
print("-"*100)
print(f'H: {horas} M: {minutos} S: {segundosFinales}')