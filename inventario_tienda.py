class InventarioTienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print(" Error: El precio y la cantidad deben ser positivos")
            return
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                producto["cantidad"] += cantidad
                print(f" Se agregaron {cantidad} unidades más de {nombre}")
                return
        
        self.productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"Producto '{nombre}' agregado al inventario")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad <= 0:
                    print(" Error: La cantidad debe ser positiva")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print("Venta realizada: {cantidad} unidades de {nombre}.")
                    if producto["cantidad"] == 0:
                        print("El producto '{nombre}' se ha agotado")
                    return
                else:
                    print("Error: No hay suficiente stock disponible")
                    return
        print(" Error: El producto no existe en el inventario")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío")
            return
        print(f"Inventario de {self.nombre}:")
        for producto in self.productos:
            print(f"  {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        print()

    def producto_mas_caro(self):
        if not self.productos:
            print("No hay productos en el inventario")
            return
        producto_caro = max(self.productos, key=lambda p: p["precio"])
        print(f" El producto más caro es '{producto_caro['nombre']}' con un precio de {producto_caro['precio']}")


tienda = InventarioTienda("Mi Tienda")

while True:
    print("----MENÚ DE OPCIONES----")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Consultar producto más caro")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad: "))
            tienda.agregar_producto(nombre, precio, cantidad)
        except ValueError:
            print("Error: Precio debe ser número y cantidad debe ser entero")

    elif opcion == "2":
        nombre = input("Nombre del producto a vender: ")
        try:
            cantidad = int(input("Cantidad a vender: "))
            tienda.vender_producto(nombre, cantidad)
        except ValueError:
            print("Error: La cantidad debe ser un número entero")

    elif opcion == "3":
        tienda.mostrar_inventario()

    elif opcion == "4":
        tienda.producto_mas_caro()

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intenta de nuevo")
