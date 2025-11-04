totalcompra = 0
i = 0

precio_mango = 1000
precio_fresa = 2000
precio_manzana = 3000

while True:
    print("menu de opciones")
    print("1.mango")
    print("2.fresa")
    print("3.manzana")
    print("s.salir")
    opcion = input("ingrese una opcion: ")

    if opcion in ["S", "s"]:
        print("gracias por su compra")
        break
    elif opcion == "1":
        cantidad = int(input("ingrese la cantidad: "))
        total = precio_mango * cantidad
    elif opcion == "2":
        cantidad = int(input("ingrese la cantidad: "))
        total = precio_fresa * cantidad
    elif opcion == "3":
        cantidad = int(input("ingrese la cantidad: "))
        total = precio_manzana * cantidad
    else:
        print("opcion no valida")
        continue

    totalcompra = totalcompra + total
    i = i + 1
    print("usted compro ", cantidad, "para un total de ", total)
    
print("el total a pagar es: ", totalcompra)
if i > 0:
    promedio = totalcompra / i
    print("el promedio de compra es: ", promedio)
else:
    print("no se realizaron compras")
