#Titulo: Se verifica si el usuario aprobo o no aprobo
#Entradas:
#   Se ingresa la nota 
#Salida:
#   Si cumple los requerimientos arroja un mensaje
#Proceso
#   Se ingresa la nota, si la nota es mayor a 60 inprime "Aprobo" si la nota es menor a 60 inprime "No aprobo"
nota = float(input(f"Ingrese su nota"))
if nota < 60:
    print ("No Aprobo")
else:
    print ("Aprobo")
