##Ejercicio 1
notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mayor = 0
menor = 100
promedio = 0

for i in notas:
    promedio += i
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i

print("Las notas son =")
for i in notas:
    print((i))
print(f"La mayor es {mayor} y la menor {menor}")
print(f"El promedio de las notas es {promedio}")

##Ejercicio 2
lista = []

for i in range(5):
    lista.append(input(f"Ingrese el producto numero {i+1} "))

lista_ordenada = sorted(lista)

eliminar = input(f"Que producto desea eliminar de la lista? {lista_ordenada}")
lista_ordenada.remove(eliminar)
print("La lista de productos es =")
for i in lista_ordenada:
    print(i)

##Ejercicio 3
import random

lista = [random.randint(1,100) for i in range(15)]
for i in lista:
    print(i)

lista_par = [i for i in lista if i % 2 == 0]
lista_impar = [i for i in lista if i % 2 != 0]

print("Los numeros pares son = ")
for i in lista_par:
    print(i)
print(f"la cantidad de numeros pares son = {len(lista_par)}")

print(f"Los numeros impares son =")
for i in lista_impar:
    print(i)
print(f"La cantidad de numeros impares son = {len(lista_impar)}")

##Ejercicio 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista = []

for i in datos:
    if i not in lista:
        lista.append(i)
        
print("La lista original es =")
for i in datos:
    print(i)
print("La lista sin numeros repetidos es =")
for i in lista:
    print(i)

##Ejercicio 5
alumnos = ["Colidio", "Galoppo", "Quintero", "Armani", "Montiel", "Driussi", "Bustos", "Salas"]
for i in alumnos:
    print(i)

opcion = input("Desea agregar (A) o eliminar (E) un alumno a la lista ")

if opcion == 'A':
    alumnos.append(input("Ingrese el alumno a agregar = "))
elif opcion == 'E':
    alumnos.remove(input("Ingrese el alumno a eliminar = "))

print("La lista actualizada es =")
for i in alumnos:
    print(i)

##Ejercicio 6
lista = [1, 2, 3, 4, 5, 6, 7]

ultimo = lista[-1]

lista_corrida = [ultimo] + lista[:-1]

print("Lista original:")
for i in lista:
    print(i)

print("Lista corrida una posicion a la derecha:")
for i in lista_corrida:
    print(i)

##Ejercicio 7
temperaturas = [
    [11, 21],
    [9, 22],
    [9, 22],
    [11, 20],
    [13, 21],
    [12, 22],
    [11, 21]
]

suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(len(temperaturas)):
    temp_min, temp_max = temperaturas[i]

    suma_min += temp_min
    suma_max += temp_max

    amplitud = temp_max - temp_min
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"Promedio de minimas : {promedio_min}")
print(f"Promedio de maximas : {promedio_max}")
print(f"El dia de mayor amplitud fue : {dia_mayor_amplitud} Amplitud {mayor_amplitud})")

##Ejercicio 8
notas = [
    [10, 5, 7],
    [8, 6, 8],
    [4, 6, 7],
    [2, 8, 6],
    [7, 4, 5]
]

print("Promedio de cada estudiante : ")
for i, alumno in enumerate(notas):
    promedio_alumno = sum(alumno) / len(alumno)
    print(f"Alumno {i+1} : {promedio_alumno}")

    print("Promedio de cada materia :")
    numero_materias = len(notas[0])
    for j in range(numero_materias):
        suma_materias = sum(notas[i][j] for i in range(len(notas)))
        promedio_materia = suma_materias / len(notas)
        print(f"Materia {j+1} : {promedio_materia}")

##Ejercicio 9
tateti = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

for fila in tateti:
    print(" ".join(fila))
print()

jugador = 'X'

for turno in range(9):
    print(f"Jugador = {jugador}")

    fila = int(input("Ingrese el numero de fila (0-2) : "))
    columna = int(input("Ingrese el numero de columna (0-2) :"))

    if tateti[fila][columna] == "-":
        tateti[fila][columna] = jugador

        for i in tateti:
            print(" ".join(i))
        print()

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
    else:
        print("Elija otro casillero")

##Ejercicio 10
productos = [
    [1,2,3,4,5,6,7],
    [2,3,4,5,6,7,8],
    [3,4,5,6,7,8,9],
    [4,5,6,7,8,9,10]
]

print("Total vendido por cada producto :")
total_producto = []
for i in range(len(productos)):
    total = 0
    for j in range(len(productos[i])):
        total += productos[i][j]
    total_producto.append(total)
    print(f"Producto numero {i+1} total = {total}")

dia_mayor_venta = 0
dia_mayor_indice = 0
for i in range(7):
    total_dia = 0
    for j in range(4):
        total_dia += productos[i][j]
    
    if total_dia > dia_mayor_venta:
        dia_mayor_venta = total_dia
        dia_mayor_indice = j + 1
        
print(f"El dia con mayor ventas totales fue : {dia_mayor_indice}, total = {dia_mayor_venta}")

producto_mayor_venta = 0
producto_indice = 0
for i in range(4):
    if total_producto[i] > producto_mayor_venta:
        producto_mayor_venta = total_producto[i]
        producto_indice = i + 1

print(f"El producto mas vendido de la semana es : {producto_indice}, total = {producto_mayor_venta}")
