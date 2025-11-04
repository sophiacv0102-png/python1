num = int(input("ingrese un numero entero positivo: "))
for x in range(1, num + 1, 2): # el rango empieza en 1, termina en num e incrementa de 2 en 2 y el num + 1 es para incluir el numero ingresado en caso de que sea impar
    if x < num - 1: # esta condicion es para que no imprima la coma despues del ultimo numero
        print(str(x) + ",", end=" ") #el end imprimen en la misma linea 
    else:
        print(str(x)) # imprime el ultimo numero sin coma