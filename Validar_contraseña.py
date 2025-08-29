#Nombre: Programa para validar la contraseña de administrador
#Entradas: 
#La contraseña ingresada por el usuario
#Proceso de Salida: 
#Mediante la función if y else determina si la contraseña coincide con la establecida (12344)
#Salida:
#El mensaje final que recibe el usuario, que puede ser 
#"Usted tiene permisos de administrador" o "Usted no tiene permisos"
contraseña = float(input("Ingrese su contraseña: "))
if contraseña == 54321:
    print("Usted tiene perrmisos de administrador")
else:
    print("Usted no tiene permisos")