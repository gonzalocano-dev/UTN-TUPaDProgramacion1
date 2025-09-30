#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario(input("Ingrese su nombre: "))

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
import math

def calcular_area_circulo(radio):
    radio = radio**2
    return radio * math.pi

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo: "))

print(f"El area del circulo es : {calcular_area_circulo(radio)} y su perimetro : {calcular_perimetro_circulo(radio)}")

#Ejercicio 5
def segundos_a_hora(segundos):
    return segundos/3600

segundos = float(input("Ingrese la cantidad de segundos: "))

print(f"{segundos} segundos son {segundos_a_hora(segundos)} horas")

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(10):
        tabla = numero * (i + 1)
        print(f"{numero} X {i + 1} = {tabla}")

tabla_multiplicar(int(input("Ingrese un numero: ")))

#Ejercicio 7
def operaciones_basicas(a, b):
    print(f"Suma {a} + {b} = {a + b}")
    print(f"Resta {a} - {b} = {a - b}")
    print(f"Multiplicacion {a} X {b} = {a * b}")
    print(f"Division {a} / {b} = {a / b}")

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese un segundo numero: "))

operaciones_basicas(a, b)

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Ingrese su peso en kilogramos: ").replace(",", "."))
altura = float(input("Ingrese su altura en metros: ").replace(",", "."))

print(f"Su indice de masa corporal es = {calcular_imc(peso, altura)}")

#Ejercicio 9
def celsius_a_farenheit(celsius):
    return (celsius * (9 / 5) + 32)

celsius = float(input("Ingrese la temperatura en grados celsius: ").replace(",", "."))

print(f"{celsius}°C equivalen a {celsius_a_farenheit(celsius)}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese un segundo numero: "))
c = float(input("Ingrese un tercer numero: "))

print(f"El promedio de los 3 numeros ingresados es = {calcular_promedio(a, b, c)}")