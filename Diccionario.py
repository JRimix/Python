#Diccionarios
#Permite almacenar valores de diferente tipo e incluso listas
#La principal caracteristia es que los datos se almacenan asociados a una clave : valor para cada elemento
#el orden es indiferente, a cada valor se le asigna una clave unica, independientemente del lugar 0,1,2,3

midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["Francia"])
#se declara entre llaves, y los elementos se asocian en parejas o mas con dos puntos
#clave seria en el ejemplo el pais y el valor la ciudad capital
print(midiccionario)
midiccionario["Italia"]="Lisboa"
#Agregar valor
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
#delete
print(midiccionario)

tupla=["España", "Francia", "Reino", "Alemania"]
diccionario={tupla[0]:"Madrid", tupla[1]:"Paris", tupla[2]:"Londres", tupla[3]:"Berlin"}
print(diccionario)
print(diccionario["Alemania"])
#se puede agregar otro diccionario adentro siempre indicando con llaves {}

print(diccionario.keys())
#devuelve las claves del diccionario
print(diccionario.values())
#devuelve los valores de las claves
print(len(diccionario))
#devuelve la longitud del diccionario
