# SERIE A B A B A...
# A = interruptor

n = int(input('Ingrese un numero: '))

a = 0
for i in range(1,n+1):
    if a == 0:
        print('A')
        a = 1
    else:
        print('B')
        a = 0
print(a)