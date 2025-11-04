cantidad_personas = int(input("ingrese la cantidad de personas: "))
if cantidad_personas <= 0:
    print("error")
else: #solicitar datos de cada persona y calcular promedios de edad y altura
    promedio_edad = 0
    promedio_altura = 0
    for x in range(1, cantidad_personas + 1):
        print("solicitando datos persona #" + str(x))#edad           promedio_edad = romedio_edad + edad 
        nombre = input("ingrese su nombre: ")
        edad = int(input("ingrese su edad: "))
        altura = float(input("ingrese su altura en metros: "))
        print()

        promedio_edad = promedio_edad + edad
        promedio_altura = promedio_altura + altura
        
    promedio_edad = promedio_edad / cantidad_personas
    promedio_altura = promedio_altura / cantidad_personas
if promedio_edad <15 and altura <1.55:
            print("el promedio de edad es: " + str(promedio_edad) + " y el promedio de altura es: " + str(promedio_altura) + " su altura es baja para su edad")
elif promedio_edad >5 and altura >1.68:
            print("el promedio de edad es: " + str(promedio_edad) + " y el promedio de altura es: " + str(promedio_altura) + " vas a ser alto")
else:
            print("el promedio de edad es: " + str(promedio_edad) + " y el promedio de altura es: " + str(promedio_altura) + " su altura es buena")
