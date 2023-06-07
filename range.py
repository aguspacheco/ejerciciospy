#SUMA LOS PRIMEROS N NUMEROS CON LA FUNCION RANGE

a = int(input('Ingrese un numero: '))
suma = 0

for i in range(1, a+1):
    suma = suma + i

print('La suma de los primeros N numeros hasta ' , a, 'Es: ', suma)
