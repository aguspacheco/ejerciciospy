#NUMERO MAYOR QUE EL ANTERIOR 

valor = int(input('¿Cuantos valores vas a ingresar?\n '))

if valor < 1:
    print('ERROR')
else:
    a = int(input('Escriba un numero: '))
    for i in range(valor - 1):
        b = int(input(f'Ingrese un numero mas grande que el {a}:'))
        if b <= a:
            print(f'{b} :no es mayor que: {a}')
        a = b
    print('Gracias👍')