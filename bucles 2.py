#Bluce tipo for RANGE y concatenar

for i in range(5):
   print(f"valor de la variable {i}")

# notacion: agregando la f nos permite concatenar y jugar con formatos distintos

for i in range(5,10):
   print(f"valor de la variable {i}")
#se puede ingresar rangos en el range, incluye el primero (5) y excluye el ultimo (19)

for i in range(5,10,3):
   print(f"valor de la variable {i}")

#range admite un 3 argumento, en este caso le decimos que nos indique de 3 en 3

valido=False
email=input("introduce mail: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")

