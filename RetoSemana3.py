inventario = {}

while True:
    print("\n--- Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar inventario")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del producto: ").strip()
        while True:
            try:
                precio = float(input(f"Ingrese el precio de '{nombre}': "))
                if precio < 0:
                    print("El precio debe ser un valor positivo.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número válido para el precio.")

        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad disponible de '{nombre}': "))
                if cantidad < 0:
                    print("La cantidad debe ser un valor no negativa.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número entero válido para la cantidad.")

        if nombre in inventario:
            print(f"¡Advertencia! El producto '{nombre}' ya existe en el inventario.")
            actualizar = input("¿Desea actualizar su precio y cantidad? (si/no): ").lower()
            if actualizar == 'si':
                inventario[nombre] = (precio, cantidad)
                print(f"El producto '{nombre}' ha sido actualizado.")
            else:
                print(f"No se realizaron cambios al producto '{nombre}'.")
        else:
            inventario[nombre] = (precio, cantidad)
            print(f"El producto '{nombre}' ha sido añadido al inventario.")

    elif opcion == '2':
        nombre = input("Ingrese el nombre del producto que desea consultar: ").strip()
        if nombre in inventario:
            precio, cantidad = inventario[nombre]
            print(f"Detalles de '{nombre}':")
            print(f"  Precio: ${precio:.2f}")
            print(f"  Cantidad disponible: {cantidad}")
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")
    elif opcion == '3':
        nombre = input("Ingrese el nombre del producto cuyo precio desea actualizar: ").strip()
        if nombre in inventario:
            while True:
                try:
                    nuevo_precio = float(input(f"Ingrese el nuevo precio para '{nombre}': "))
                    if nuevo_precio < 0:
                        print("El precio debe ser un valor positivo.")
                    else:
                        _, cantidad_actual = inventario[nombre]
                        inventario[nombre] = (nuevo_precio, cantidad_actual)
                        print(f"El precio de '{nombre}' ha sido actualizado a ${nuevo_precio:.2f}.")
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio.")
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")
    elif opcion == '4':
        nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip()
        if nombre in inventario:
            del inventario[nombre]
            print(f"El producto '{nombre}' ha sido eliminado del inventario.")
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")

    
    elif opcion == '5':
        valor_total = sum(precio * cantidad for precio, cantidad in inventario.values())
        print(f"El valor total del inventario es: ${valor_total:.2f}")
    elif opcion == '6':
        if not inventario:
            print("El inventario está vacío.")
            

        print("\n--- Inventario Actual ---")
        for nombre, (precio, cantidad) in inventario.items():
            print(f"Producto: {nombre}, Precio: ${precio:.2f}, Cantidad: {cantidad}")
        print("-------------------------\n")

    elif opcion == '7':
        print("¡Gracias por usar el gestor de inventario!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

