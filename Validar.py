#Nombre: Programa para validar si el usuario es administrador
#Entradas: 
#La contraseña ingresada por el usuario
#Proceso de Salida: 
#Mediante la función if y else determina si la contraseña ingresada es igual a "Admin"
#Salida:
#El mensaje final que recibe el usuario, que puede ser 
#"Usted es Administrador" o "Usted no es administrador"
contraseña = input("Ingrese su contraseña: ")
if contraseña == ("Admin"):
    print("Usted es Administrador")
else:
    print("Usted no es administrador")