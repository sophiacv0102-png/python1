print("Metodos de envio")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. SALIR")
method = int(input("Ingrese el método HTTP (1-5): "))
while (method!=5):
    match method:
        case 1:
            print("fetching resource")
        case 2:
            print("creating resource")  
        case 3:
            print("updating resource")
        case 4:
            print("deleting resource")
        case 5:
            print("salir")
        case _:
            print("unsupported HTTP method")
    print("Metodos de envio")
    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. DELETE")
    print("5. SALIR")
    method = int(input("Ingrese el método HTTP (1-5): "))
print("gracias por usar el programa")