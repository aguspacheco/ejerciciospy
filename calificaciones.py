#CALIFICACIONES DE ALUMNOS Y SEGUN SU NOTA MUESTRA UN MENSAJE 
#DATOS: #N: NOTA R: RESPUESTA

N = float (input("Ingrese una nota:"))

if N <= 5:
    R = 'El alumno desaprobo'
elif N <= 6:
    R = 'El alumno aprobo'
elif N <= 8:
    R = 'El alumno promociono'
else:
    R = 'Nota excelente'

print('La nota: ',N,R)