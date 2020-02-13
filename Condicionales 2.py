#PY permite concatenar condicionales para analisis complejos de varias condiciones
#PY prescinde del condicional switch a diferencia de otros lenguajes
#CONCATENACION

edad=-7

if 0<edad<100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

#se agrega antes de la condicion un operador (0<). evalua de izq a der

salario_presi=int(input("introduce salario presi"))
print("Salario presi: "+ str(salario_presi))

salario_dire=int(input("introduce salario dire"))
print("Salario dire: "+ str(salario_dire))

salario_jefe=int(input("introduce salario jefe"))
print("Salario jefe: "+ str(salario_jefe))

salario_admin=int(input("introduce salario admin"))
print("Salario admin: "+ str(salario_admin))

if salario_admin<salario_jefe<salario_dire<salario_presi:
    print("salarios justos")
else:
    print("salarios no justos")

#AND / OR

print("Programa Becas")
distancia_escuela=int(input("Introduce distancia en KM "))
print(distancia_escuela)

numero_hermanos=int(input("Numero de hermanos "))
print(numero_hermanos)

salario_familia=int(input("salario familiar "))
print(salario_familia)

if distancia_escuela>40 and numero_hermanos>2 and salario_familia<=20000:
    print("Tienes una Beca para ti")

else:
    print("No tienes derecho a Beca para ti")

#OPERADOR IN

print("asignaturas optativas")
print("grafica - pruebas de soft - UX")

opcion=input("escribe la asignatura que quieras: ")

asignaturas=opcion.lower()

if asignaturas in ("grafica", "pruebas de soft", "ux"):
    print("asignatura elegida " + asignaturas)
else:
    print("Asignatura no disponibile")

#PY es case sensitive = distingue entre mayusculas y minisculas. EJ= si escribo asignatura Grafica con May va a dar error
#Lower: transformar en miniscula funcion lower




