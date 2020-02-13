edad = 18
minimo = 5
maximo = 100

edad_usuario = int(input("Que edad tienes: "))

if edad_usuario >= edad and edad_usuario < maximo:
    print("Es mayor de edad")
elif edad_usuario > maximo:
    print("Eres muy grande")
elif edad_usuario <= minimo:
    print("Eres muy chico")
else:
    print("Es menor de edad")

Mayor = False

Es_mayor = int(input("Dime tu edad: "))

if Es_mayor >= edad:
    Mayor = True
    print("Es el usuario mayor de edad? ", Mayor)
else:
    print("Es menor")

def adulto(a):
    if a >= edad:
        Mayor = True
        print(Mayor)
    else:
        print("Es menor")
adulto(18)






