#CALCULA EL FACTORIAL DE UN NUMERO INGRESADO

n = int (input('Ingrese un numero: '))

if n <= 0:
    print('Ingrese un numero positivo')
else:
    f = 1
    for i in range (1, n + 1):
        f = f * i
    print(f'El factorial de {n} es {f} ')