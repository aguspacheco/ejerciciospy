#DETERMINA SI UN NUMERO ES PAR  O IMPAR 
n1 = int(input('Ingrese un numero: '))
n2 = int(input(f'Ingrese otro numero mayor o igual que {n1:} '))

if n2 < n1:
    print(f'Ingrese un mayor o igual que {n1}')
else:
    for i in range(n1, n2+1):
        if i  % 2 == 0:
            print(f'El numero {i} es par')
        else:
            print(f'El numero {i} es impar')  
