#Ejercicio 1
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
}

precios_frutas.update({'Naranja' : 1200, 'Manzana' : 1500, 'Pera' : 2300})

print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#Ejercicio 4
contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto N°{i+1}: ")
    celular = input(f"Ingrese el numero de celular del contacto N°{i+1}: ")

    contactos[nombre] = celular

lista_contactos = list(contactos.keys())

while True:
    print(f"Desea consultar el numero de alguno de estos contactos? \n {lista_contactos}")
    nombre = input("Contacto (Inserte SALIR si desea cancelar): ")

    if nombre.lower() == 'salir':
        print("Saliendo.")
        break

    if nombre not in contactos:
        print("Contacto inexistente.")
    else:
        print({contactos[nombre]})
        input()

#Ejercicio 5
frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

palabras_repetidas = {}

for palabra in palabras:
    if palabra in palabras_repetidas:
        palabras_repetidas[palabra] += 1
    else:
        palabras_repetidas[palabra] = 1

print(f"Palabras unicas: {palabras_unicas}")
print(f"Recuento: {palabras_repetidas}")

#Ejercicio 6
alumnos = []

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota_1 = float(input("Ingrese la primer nota: "))
    nota_2 = float(input("Ingrese la segunda nota: "))
    nota_3 = float(input("Ingrese la tercer nota: "))

    alumno = (nombre, nota_1, nota_2, nota_3)
    alumnos.append(alumno)

for nombre, nota_1, nota_2, nota_3 in alumnos:
    promedio = (nota_1 + nota_2 + nota_3) / 3
    print(f"{nombre} ({nota_1}, {nota_2}, {nota_3}) Promedio : {promedio}")

#Ejercicio 7
parcial_1 = {"Ana", "Luis", "María", "Carlos", "Sofía"}
parcial_2 = {"Luis", "María", "Pedro", "Sofía", "Lucía"}

ambos = parcial_1 & parcial_2
print("Aprobaron los dos parciales: ", ambos)

solo_uno = parcial_1 ^ parcial_2
print("Aprobaron solo uno de los dos parciales: ", solo_uno)

al_menos_uno = parcial_1 | parcial_2
print("Aprobaron al menos un parcial: ", al_menos_uno)

#Ejercicio 8
productos = {
    "Disco de vinilo" : 25,
    "CD" : 15,
    "Pen-Drive" : 20
}

opcion = ""
while opcion != "4":
    print("\n==== MENU DISQUERIA ====")
    print("1) Consultar Stock")
    print("2) Agregar Stock")
    print("3) Agregar producto")
    print("4) Salir")
    opcion = input("Opcion: ").strip()

    lista_productos = list(productos.keys())

    match opcion:
        case "1":
            print(lista_productos)
            nombre = input("Ingrese el nombre del producto a consultar: ")
            if nombre in productos:
                print(f"{nombre} - Stock = {productos[nombre]} unidades")
                input()
            else:
                print("Producto inexistente!")
                input()

        case "2":
            print(lista_productos)
            nombre = input("Ingrese el nombre del producto a agregar stock: ")
            if nombre in productos:
                unidades = int(input("Ingrese la cantidad de unidades: "))
                productos[nombre] += unidades
                print(f"Nuevo stock de {nombre} - {productos[nombre]} unidades")
                input()
            else:
                print("Producto inexistente!")
                input()
        
        case "3":
            nombre = input("Ingrese el nombre del nuevo producto: ")
            if nombre in productos:
                print("El producto ya existe!")
                input()
            else:
                unidades = int(input("Ingrese la cantidad de unidades del nuevo producto: "))
                productos[nombre] = unidades
                print(f"Agregado el producto {nombre} con {unidades} unidades")
                input()
        case "4":
            print("Fin del programa.")
            input()
            break
        case _:
            print("Opcion invalida.")
            input()

#Ejercicio 9
agenda = {
    ("lunes", "12:00"): "Sacar milanesas del freezeer",
    ("martes", "18:00"): "Ir al gimnasio",
    ("miercoles", "11:00"): "Visitar a mi madre",
    ("jueves", "18:00"): "Gimnasio, devuelta",
    ("viernes", "17:00"): "Turno en la barberia",
    ("sabado", "11:00"): "Gimnasio, por ultima vez",
    ("domingo", "10:00"): "Arrancar el fuego"
}

while True:
    dia = input("Ingrese el dia a consultar actividades (CANCELAR para cortar el programa): ").lower()
    hora = input("Ingrese la hora a consultar actividad (formato HH:MM): ")

    actividad = agenda.get((dia, hora))

    if actividad:
        print(f"Actividad programada: {actividad}")
        input()
    elif dia == "cancelar":
        print("Programa terminado.")
        break
    else:
        print("No hay nada programado para ese dia y horario")
        input()

#Ejercicio 10
original = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Belgica": "Bruzelas",
    "Papua Nueva Guinea": "Puerto Moresby"
}

invertido = {capital: pais for pais, capital in original.items()}

print(f"Original: {original}")
print(f"Invertido: {invertido}")