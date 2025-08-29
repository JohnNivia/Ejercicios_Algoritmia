#Nombre: Verificar si el numero esta en el rango de -100 a 100
#Entradas:
#   Ingresa el numero
#Salida:
#   Inprime un mensaje si el numero esta entre -100 a 100 
#Proceso:
#   Se indica un numero, si el numero esta entre -100 y 100 se inprime "El numero esta dentro del rango", si al contrario el numero esta fuera del rango "El numero esta fuera del rango"
numero = float(input("Ingrese el numero"))
if numero > 100 or numero < -100:
    print ("El numero esta fuera del rango (100, -100)")
else:
    print ("El numero esta dentro del rango")