palabra = "KEVIN".lower()
match palabra:
    case "kevin":
        print("hola kevin")
    case "sofia":
        print("hola sofia")
    case _:
        print("usuario no reconocido")