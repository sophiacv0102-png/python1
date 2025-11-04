print("menu de opciones")
print("1.mango")
print("2.fresa")
print("3.manzana")
print("s.salir")
precio_mango = 1000
precio_fresa = 2000
precio_manzana = 3000
opcion = input("ingrese una opcion: ")
while opcion not in ["1", "2", "3", "s"]:
    print("opcion no valida")
    opcion = input("ingrese una opcion: ")
if opcion == "1":
    cantidad = int(input("ingrese la cantidad: "))
    total = precio_mango * cantidad
    print("el total a pagar es: ", total)
elif opcion == "2":
    cantidad = int(input("ingrese la cantidad: "))
    total = precio_fresa * cantidad
    print("el total a pagar es: ", total)
elif opcion == "3":
    cantidad = int(input("ingrese la cantidad: "))
    total = precio_manzana * cantidad
    print("el total a pagar es: ", total)
else:
    print("gracias por su compra")