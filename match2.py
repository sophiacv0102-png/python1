print("Metodos de envio")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. SALIR")
method = str(input("Ingrese el método: "))
match method.upper():
    case "GET":
        print("fetching resource")
    case "POST":
        print("creating resource")  
    case "PUT":
        print("updating resource")
    case "DELETE":
        print("deleting resource")
    case _:
        print("unsupported HTTP method")