#Nombre: Se indica si el usuario puede votar
#Entradas:
#   Se ingresa la edad y la nacionalidad del usuario
#Salida:
#   Aparece un mensaje si cumple las condiciones sino aparece otro mensaje
#Proceso:
#   Dependiendo la edad y la nacionalidad inprime un mensaje, si el usuario es mayor de edad y es colombiano aparece "Usted puede votar" si es menor de edad o no es colombiano aparece "Usted no puede votar"

Edad = float(input("Ingrese su edad"))
Nacionalidad = input("Ingrese su nacionalidad")
if Edad >= 18 and Nacionalidad == "Colombiana":
    print("Usted puede votar")
else:
    print("Usted no puede votar")