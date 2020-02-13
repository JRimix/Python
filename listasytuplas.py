list=["maria", "pepe", "Marta", "Antonio"]

print(list[:])

print(list[3])

print(list[-2])
#cuando utilizamos el - empieza desde atras y el primer elemento es -1; en lugar 0

print(list[0:3])
#porciones, incluye el primer elemento y omite el ultimo indicado en el print

print(list[2:])
#ejecuta desde el valor indicado inclusive en adelante -->

list.append("Javi")
#agrega valor al final de la lista

list.insert(2,"Javi")
#insertar en posicion especifica
print(list)

list.extend(["Sandra", "Ana", "Lucia"])
#extender
print(list)

print(list.index("Javi"))
#en que indice esta x? devuelve posicion ò indice del valor buscado

print("Javi" in list)
#devuelve  true o false en caso que el valor buscado este en la lista

list.remove("Ana")

print(list)

list.pop()
#elimina el ultimo elemento de la lista

print(list)

list2=["angel", "carlitos"]*3

list3=list+list2
#Sumar listas

print(list3)

#listas pueden multiplicarse EJ = list(xx)*3

#TUPLAS. Son listas inmutables, no podemos modificarla, añadir (append) , mover, eliminar elementos (remove)
#Son mas rapidas, menos espacio, formatean strings, pueden utilizarse como claves en un diccionario
#Permiten extraer porciones siendo el resultado una tupla nueva
#Permiten comprobar si un elemento se encuentra en la tupla y buscarlo (index)
#Van entre () a diferencia de las listas que van en [], aunque son opcionales

tupla=("Juan", 13,1,1995)
tupla=tuple(tupla)
print(tupla[0])
print(tupla)
#List y tuple funciones para convertir una lista en tupla y viceversa

#Funcion count consulta cuantos valores hay
print(tupla.count(13))

#Funcion len consulta la longitud de elementos en tupla

nombre, dia, mes, agno=tupla
print(nombre)
print(dia)
print(agno)
print(mes)
#Desempaquetado de Tuplas.




















