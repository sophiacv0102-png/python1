print("Metodos de envio")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. SALIR")
method = str(input("Ingrese el método: "))
match method.lower():
    case "get":
        print("fetching resource")
    case "post":
        print("creating resource")  
    case "put":
        print("updating resource")
    case "delete":
        print("deleting resource")
    case _:
        print("unsupported HTTP method")