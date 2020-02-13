
def mayor (numero1, numero2):
    if numero1 > numero2:
        print("numero 1 es mayor")
    elif numero2 > numero1:
        print("numero 2 es mayor")
    else:
        print("son iguales")

mayor(8, 2)

meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
)

Salir = False

while(not Salir):
    numero = int(input("Dame un numero: "))

    if numero==0:
        Salir=True
    else:
        if(numero>=1 and numero<=len(meses)):
            print(meses[numero-1])
        else:
            print("Inserta un numero entre 1 y ",len(meses))

##########Cadena sin espacios ############################

cadena = input("Dame una cadena: ")

print(cadena)

lista = []

for c in cadena:
    if (c != ' '):
        lista.append(c)

print(lista)

