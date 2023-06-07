#CUENTA EL NUMERO DE VOCALES EN UNA FRASE INGRESADA.

a = str(input('Ingrese una frase: '))
v = 'aeiouAEIOU'

i = 0
cantVocales = 0

for i in a:
    if i in v:
        cantVocales = cantVocales + 1

print('La cantidad de vocales que tiene la frase es: ' + str(cantVocales))