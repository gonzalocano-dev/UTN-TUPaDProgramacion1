#Ejercicio numero 1
print("Hola mundo!")

#Ejercicio numero 2
nombre = input("Ingrese su nombre ")

print(f"Hola", nombre) 

#Ejercicio numero 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Mi nombre es", nombre, apellido, ", tengo", edad, "años y vivo en", residencia)

#Ejercicio numero 4
import math

radio = int(input("Ingrese el radio del circulo: "))

perimetro = 2 * math.pi * radio

area = math.pi * (radio ** 2)

print (f"Si el radio del circulo es:", radio, "el perimetro es igual a :", perimetro, "y el area es igual a:", area)

#Ejercicio numero 5
segundos = int(input("Ingrese la cantidad de segundos:"))

horas = segundos/3600

print(segundos,"segundos son igual a", horas, "horas")

#Ejercicio numero 6
numero = int(input("Ingrese un numero:"))

for i in range(11):
    print(i,"X", numero, "=", (numero * i))

#Ejercicio numero 7
while True:
    numero_1 = int(input("Ingrese el primer numero(distinto de 0):"))
    numero_2 = int(input("Ingrese el segundo numero(distinto de 0)"))
    if(numero_1 == 0 or numero_2 == 0):
        print(f"Ingrese un numero que no sea 0!")
        break
    else:
        suma = numero_1 + numero_2
        resta = numero_1 - numero_2
        producto = numero_1 * numero_2
        division = numero_1 / numero_2

        print(f"Suma:", suma, "\nResta:", resta, "\nMultiplicacion:", producto, "\nDivision:", division)
        break

#Ejercicio numero 8
altura = float(input("Ingrese su altura en metros:"))
peso =float(input("Ingrese su peso en KG:"))

imc = peso / (altura ** 2)

print(f"Su indice de masa corporal es:", imc)

#Ejercicio numero 9
grados_celsius = float(input("Ingrese una temperatura en grados Celsius:"))

grados_fahrenheit = ((9/5) * grados_celsius) + 32

print(grados_celsius, "°C son equivalentes a", grados_fahrenheit, "°F")

#Ejercicio numero 10
numero_1 = int(input("Ingrese el primer numero:"))
numero_2 = int(input("Ingrese el segundo numero:"))
numero_3 = int(input("Ingrese el tercer numero:"))

promedio = (numero_1 + numero_2 + numero_3) / 3

print(f"El promedio de los tres numeros es:", promedio)