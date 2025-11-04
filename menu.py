#como hacer un menú en python con while
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        print("Ha seleccionado la Opción 1")
    elif opcion == "2":
        print("Ha seleccionado la Opción 2")
    elif opcion == "3":
        print("Ha seleccionado la Opción 3")
    elif opcion == "4":
        print("Saliendo del menú...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
    