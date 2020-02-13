#Flujos de ejecucion: orden con el que se ejecutan instrucciones

print("Programa de evaluacion de notas")

nota_alumno=input("introduce la nota del alumno: ")
#funcion input, el programa queda a la espera de input de dato para continuar flujo de ejecucion
#se puede agregar una leyenda para sea mas facil identificar el valor q debe agregarse

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion


# se debe ingresar : para indicar que finaliza la condicion del IF (linea 11)
#atencion a las sangrias para indicar la instruccion (linea 12)
# == para igual , != diferente que

print(evaluacion(int(nota_alumno)))
#INT: debemos indicarle a py que lo que vaya en el input es numerico, en lugar de texto como lo toma

#ELSE

print("acceso")

edad_usuario=int(input("Introduce tu edad"))

if edad_usuario<18:
    print("no permitido")
elif edad_usuario>100:
    print("Edad incorrecta")
else:
    print("puedes pasar")
#else trabaja en bloque con el IF mas cercano. Desconoce los IF anterior, debe asociarse correctamente
#elif permite asociar el else a todos los condicionales del bloque, utilizar varios IF.

print("el programa finalizo")











