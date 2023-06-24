from par import ciclo_pares

n = int(input('Ingrese un numero: '))
print('Los numeros pares hasta', n, 'son: ')
for i in ciclo_pares(n):
    print(i)