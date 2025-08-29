#Nombre: Verificar si el numero es negativo
#Entradas:
#   Se ingresa un numero
#Salida:
#   Dependiendo el numero el sistema indica un mensaje
#Proceso:
#   Se selecciona un numero si el numero es negativo inprime un mensaje
numero = float(input("ingrese un numero "))
if numero < 0:
    print ("el numero es negativo")
else:
    print ("El numero no es negativo")