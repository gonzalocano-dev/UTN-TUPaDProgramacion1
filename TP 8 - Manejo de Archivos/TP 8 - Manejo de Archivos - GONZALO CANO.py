#Ejercicio 1
with open("productos.txt", "w") as archivo_productos:
    archivo_productos.write("USB, 1500, 10\n")
    archivo_productos.write("CD, 1000, 15\n")
    archivo_productos.write("Vinilo, 2000, 20\n")

#Ejercicio 2
def mostrar_productos():
    with open("productos.txt", "r") as archivo_productos:
        lineas = archivo_productos.readlines()
        for linea in lineas:
            productos = linea.strip().split(",")
            print("Producto: " + " | ".join(productos))

#Ejercicio 3
mostrar_productos()
opcion = input("Desea ingresar un producto? S/N ")
if opcion.lower() == "s":
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    with open("productos.txt", "a") as archivo_productos:
        archivo_productos.write(f"{nombre}, {precio}, {cantidad}")

#Ejercicio 4
productos = []

with open("productos.txt", "r") as archivo_productos:
    for linea in archivo_productos:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre.strip(),
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

for p in productos:
    print(p)

#Ejercicio 5
busqueda = input("Ingrese el nombre de un producto a buscar en el archivo: ")

#usando la lista ya cargada en el punto anterior
for producto in productos:
    if producto["nombre"].lower() == busqueda.lower():
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
    else:
        print(f"El producto {busqueda} no se encuentra en el archivo")


#Ejercicio 6
with open("productos.txt", "w") as archivo_productos:
    for producto in productos:
        archivo_productos.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

print("Los productos se guardaron en el archivo 'productos.txt'")