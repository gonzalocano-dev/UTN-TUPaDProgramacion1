##Ejercicio 1
for i in range(101):
    print (i)

##Ejercicio 2
numero = int(input("Ingrese un numero:"))

n = abs(numero)

digitos = 0
while n > 0:
    n //= 10
    digitos += 1

print(f"El numero {numero} tiene {digitos} cantidad de digitos")


##Ejercicio 3
numero_1 = int(input("Ingrese un primer numero:"))
numero_2 = int(input("Ingrese un segundo numero:"))

inicio = min(numero_1, numero_2) + 1
fin = max(numero_1, numero_2)

suma = 0

for i in range(inicio, fin):
    suma += i

print(f"La suma de los numeros comprendidos entre {numero_1} y {numero_2} es = {suma}")

##Ejercicio 4
suma = 0
numero = 1
while numero != 0:
    numero = int(input("Ingrese un numero:"))
    suma += numero

print(f"La suma de los numeros ingresados es = {suma}")    

##Ejercicio 5
import random
numero_aleatorio = random.randint(0, 9)

numero = int(input("Ingrese un numero y trate de adivinar:"))

while numero != numero_aleatorio:
    numero = int(input("Incorrecto! Intenta de nuevo:"))

print(f"Correcto! El numero era = {numero_aleatorio}")

##Ejercicio 6
i = 100
while i >= 0:
    print(i)
    i -= 2

##Ejercicio 7
numero = int(input("Ingrese un segundo numero:"))

suma = 0

for i in range(0, numero):
    suma += i

print(f"La suma de los numeros comprendidos entre 0 y {numero} es = {suma}")

##Ejercicio 8
cantidad = 100

positivo = 0
negativo = 0
par = 0
impar = 0

for i in range(cantidad):
    numero = int(input("Ingrese un numero:"))
    if numero > 0:
        positivo += 1
    else:
        negativo += 1
    
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"La cantidad de numeros pares son = {par}, la cantidad de impares son = {impar}, los positivos son = {positivo} y los negativos son = {negativo}")

##Ejercicio 9
cantidad = 100
suma = 0

for i in range(cantidad):
    numero = int(input("Ingrese un numero:"))
    suma += numero

media = suma / cantidad

print(f"La media de los numeros ingresados es = {media}")

##Ejercicio 10
numero = int(input("Ingresa un numero:"))

num_invertido = 0
num = numero  

while num > 0:
    digito = num % 10        
    num_invertido = num_invertido * 10 + digito  
    num = num // 10       

print(f"El numero {numero} invertido es = {num_invertido}")