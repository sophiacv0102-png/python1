#practica de python for
for i in range(5):
    print("Iteración número:", i)

#practica de python while
contador = 0
while contador < 5:
    print("Contador es:", contador)
    contador += 1

#practica de python if
numero = 10
if numero > 5:
    print("El número es mayor que 5")
else:
    print("El número es 5 o menor")

#practica de python funciones
def saludar(nombre):
    print("Hola,", nombre)
saludar("Mundo")

#practica de python listas
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)



#practica de python match case al azar
print("colores disponibles")
print("1. ROJO")
print("2. VERDE")
print("3. AZUL")
color = str(input("Ingrese un color: "))
match color.lower():
    case "rojo":
        print("Has elegido el color rojo")
    case "verde":
        print("Has elegido el color verde")  
    case "azul":
        print("Has elegido el color azul")
    case _:
        print("Color no reconocido")

#practica de python e imprimir en una sola linea
for i in range(5):
    print(i, end=' ')
print()  # para nueva línea después del bucle

