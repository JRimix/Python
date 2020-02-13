#BUCLE INDETERMINADO: WHILE (MIENTRAS)
import math

i=1

while i<=10:
    print("Ejecucion " + str(i))
    i=i+1

print("Termino la ejecucion")

edad=int(input("Introduce tu edad: "))

while edad<5 or edad>100:
    print("edad no correcta")
    edad = int(input("Introduce tu edad: "))

print("Gracias por tus datos")
print("Edad del usuario "+ str(edad))
print()

print("Calculo de raiz cuadrada")
numero=int(input("Numero: "))
intentos=0

while numero<0:
    print("Error")

    if intentos==2:
        print("Has consumido demasiados intentos.El programa ha finalizado")
        break;


    numero=int(input("Numero: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))



