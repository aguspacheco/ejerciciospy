#GENERA LOS MULTIPLOS DE 3 
# a = interruptor

n = int(input('Ingrese un numero: '))
a = 3

for i in range(1, n+1):
    print(a, end=',')
    a = a + 3