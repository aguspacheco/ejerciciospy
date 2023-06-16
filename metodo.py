#CREA UNA LISTA Y SEPARA LA LISTA EN PARES E IMPARES 
l = [3,7,9,12,8,13,2]

def separar_lista(l):
    l.sort()
    pares = []
    impares = []
    for i in l:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

pares,impares = separar_lista(l)

print (f'Numeros pares:', pares)
print(f'Numeros impares:', impares)