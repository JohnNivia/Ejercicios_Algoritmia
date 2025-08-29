#Nombre: Programa para mirar si es multiplo de 5
#Entradas:
#   numero: Se ingresa el numero
#Salida:
#   Manda un mensaje si cumple los requerimientos establecidos
#Proceso:
#Se ingresa un numero y se verifica si es multiplo de 5 si es multiplo de 5 inprime "El numero es multiplo de 5" sino se inprime "El numero no es multiplo de 5"

numero = float(input("Ingrese el numero"))
if numero % 5 == 0:
    print (f"El {numero} es multiplo de 5")
else:
    print (f"El {numero} no es multiplo")