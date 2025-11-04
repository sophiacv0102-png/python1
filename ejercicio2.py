edad = int(input("ingrese su edad: "))
for x in range(1, edad + 1, 1): # el rango empieza en 1, termina en edad e incrementa de 1 en 1
    print("ha cumplido " + str(x) + " años")
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")
    