
#ARREGLOS

n = int(input('Ingrese el tamaño del arreglo: '))
m = int (input('Ingrese otro tamaño para el arrelo: '))

arreglo = []

for i in range(0,n):
    arreglo.append(i*m)

print(arreglo)