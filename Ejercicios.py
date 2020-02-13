#Menorque

def menorqu(a, b):

    if a > b:
        print("el menor es b")
    elif b > a:
        print("el menor es a")
    else:
        print("son iguales")

menorqu(8, 10)

#Num_Max

def maximo (a, b , c):
    if a > b > c:
        print("El mayor es A")
    elif a < b > c:
        print("El mayor es B")
    elif c > b > a:
        print ("El mayor es C")
    else:
        print ("Son iguales")

maximo(9, 4, 3)

#Bucle While. Mostar los numeros del 1 al 100

i = 1

while ( i <= 100):
    print (i)
    i+=1

print("Fin del bucle")

i = 1

for i in range(1,101):
        print(i)

print("fin del bucle")

for i in "hola mundo":
    print (i)

#Mostar todos los pares del 1 al 100

for i in range(2, 101, 2):
    print(i)

for i in range (1,101):
    if (i % 2 == 0):
        print (i)
print("todos los pares")

#Generar un rango de 10 a 1

Beta = list(range(10,0,-1))

print(Beta)

# Generar un rango desde 0 hasta la longitud de la cadena “Hola mundo”

alfa = list(range(0, len("hola mundo")))

print(alfa)

# Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas
# y con los 2 primeros caracteres intercambiados

cadena1 = input("Primera cadena: ")
cadena2 = input("Segunda cadena: ")

print(cadena2[:2] + cadena1[2:]+ " " + cadena1[:2] + cadena2[2:])

#Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
#Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado.
# También poner el número de intentos requeridos.

from random import *


def generaNumeroAleatorio(minimo, maximo):
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux

        return randint(minimo, maximo)
    except TypeError:
        print("Debes escribir numeros")
        return -1


numero_buscado = generaNumeroAleatorio(1, 100)

encontrado = False
intentos = 0

while not encontrado:

    numero_usuario = int(input("Introduce el número buscado: "))

    if numero_usuario > numero_buscado:
        print("El número que buscas es menor")
        intentos = intentos + 1
    elif numero_usuario < numero_buscado:
        print("El numero que buscas es mayor")
        intentos = intentos + 1
    else:
        encontrado = True
        print("Has acertado el número correcto es ", numero_usuario, " te ha llevado ", intentos, " intentos")
