print("desea ingresar sus datos personales")
while True:
    respuesta = input("ingrese si/no: ")
    if respuesta in ["si", "no"]:
        break
    print("respuesta no valida, intente de nuevo")
if respuesta == "no":
    print("hasta luego")
    exit()
nom = (input("ingrese su nombre: "))
edad = int(input("ingrese su edad: "))
genero = input("ingrese su genero (M/F): ")
peso = float(input("ingrese su peso en kg: "))
estatura = float(input("ingrese su estatura en metros: "))
imc = peso / estatura ** 2
if genero == "F":
    if imc < 20 :
            estado = "bajo peso"
    elif imc >= 20 and imc <= 23.9 :
            estado = "normal"
    elif imc >= 24 and imc <= 28.9 :
        estado = "sobrepeso"
    elif imc >= 29 and imc <= 37 :
        estado = "obesidad"
    elif imc > 37 :
        estado = "obesidad severa"
if genero == "M":
    if imc < 22 :
        estado = "bajo peso"
    elif imc >= 20 and imc <= 24.9 :
        estado = "normal"
    elif imc >= 25 and imc <= 29.9 :
        estado = "sobrepeso"
    elif imc >= 30 and imc <= 40 :
        estado = "obesidad"
    elif imc > 40 :
        estado = "obesidad severa"

print("nombre: ", nom)
print("edad: ", edad)
print("genero: ", genero)
print("peso: ", peso, "kg")
print("estatura: ", estatura, "m")
print("IMC: ", imc)
print("su estado de imc es: ", estado)
print("gracias por usar el programa")