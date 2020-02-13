#Continue, Pass y else
#Continue: indica a donde continuar la intruccion y bucle. Salta a la sig interaccion de bucle
#Pass se usa para definir clases (ej: nulas) y casos concretos. Devuelve "null" como si no ejecutara
#Pass cuando quieres desarrollar algo despues y usas este pass para continuar trabajando

for letra in"Python":
    if letra=="h":
        continue

    print("viendo la letra: "+ letra)

#Cuando se da la condicion, el continue salta la linea siguiente, en este caso el print.

#CONTADOR CON BUCLE CONTINUE. CUENTA DE CARACTERES

nombre="Pildoras Informaticas"

contador=0

for i in nombre:

    if i==" ":
        continue
    contador+=1

print(contador)

