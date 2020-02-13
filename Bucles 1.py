#Repetir una o varias lineas de codigo
#Bucles determinados e indeterminados:
#Determinado repite una cantidad determinada de veces; indeterminado no lo tiene definido
#Sintaxis Determinado: for variable in elemento a recorrer (lista, tupla, cadena de text, etc):

for i in [1,2,3]:
    print("hola")

for i in ["a","b","c","d"]:
    print("4")

for i in ["a","b","c","d"]:
    print(i)

#PRINT: si queremos evitar saltos de linea en el print, debe agregarse print("hola", end=" ")

for c in "juan@gmail.com":
    print(c, end="")

print()
#separar bluches print()

email=False

for b in "juan@gmail.com":

    if (b=="@"):
        email=True

if email==True:
    print("email valido")
else:
    print("email incorrecto")

#PY imprime el bucle segun cada caracter cuando no se usan listas, tuplas, etc.

#EJERCICIO de mejora de codigo

contador=0

Mail=input("introduce tu mail: ")

for h in Mail:
    if(h=="@" or h=="."):

        contador=contador+1
if contador==2:
    print("email valido")
else:
    print("no valido")

#range es considerada una funcion, un tipo de array (lista en orden, inicial 0)

for m in range(4):
    print("ejemplo range")



