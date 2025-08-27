#Ejercicio 1
#///////////////////////////////////
edad = int(input("Ingrese su edad:"))

if edad >= 18:
    print("Es mayor de edad.")

#Ejercicio 2
#///////////////////////////////////
nota_minima = 6
nota = float(input("Ingrese su nota:"))

if nota >= nota_minima:
    print("Aprobado!")
else:
    print("Desaprobado!")

#Ejercicio 3
#///////////////////////////////////
numero = int(input("Ingrese un numero:"))

if (numero % 2) == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")

#Ejercicio 4
#///////////////////////////////////
edad = int(input("Ingrese su edad:"))

if edad < 12:
    print("Usted es un niño/a.")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente.")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto/a joven.")
elif edad >= 30:
    print("Usted es un adulto/a.")

#Ejercicio 5
#///////////////////////////////////
contraseña = input("Ingrese una contraseña:")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta!")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
#///////////////////////////////////
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo!")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo!")
elif media == mediana and media == moda and mediana == moda:
    print("No hay sesgo!")

#Ejercicio 7
#///////////////////////////////////
string = input("Ingrese una frase o palabra:")

if string[-1] in "aeiou":
    print(f"{string}!")
else:
    print(string)

#Ejercicio 8
#///////////////////////////////////
nombre = input("Ingrese su nombre:")

opcion = int(input("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#Ejercicio 9
#///////////////////////////////////
magnitud = int(input("Ingrese la magnitud del terremoto:"))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7:
    print("Extremo")

#Ejercicio 10
#///////////////////////////////////
hemisferio = input("Ingrese el hemisferio en el cual se encuentra: (N/S)")
mes = int(input("Ingrese el mes del año:"))
#comento el año por que no lo estoy usando
#año = int(input("Ingrese el año:"))
dia = int(input("Ingrese el dia:"))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes == 1 or mes == 2):
        print("Usted se encuentra en Invierno!")
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes == 4 or mes == 5):
        print("Usted se encuentra en Primavera!")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes == 7 or mes == 8):
        print("Usted se encuentra en Verano!")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes == 10 or mes == 11):
        print("Usted se encuentra en Otoño!")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes == 1 or mes == 2):
        print("Usted se encuentra en Verano!")
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes == 4 or mes == 5):
        print("Usted se encuentra en Otoño!")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes == 7 or mes == 8):
        print("Usted se encuentra en Invierno!")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes == 10 or mes == 11):
        print("Usted se encuentra en Primavera!")