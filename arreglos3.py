#CALCULA 10 NUMEROS ALEATORIOS

import random

def vector_aleatorio(n):
    vector = [0]*n
    for i  in range(n):
        vector[i] = random.randint(0,16)
    return vector
    
print('Cuantos numeros aleatorios queres tenes?: ')
n = int(input())

aleatorio = vector_aleatorio(n)

print(aleatorio)

