#Nombre: Se verifica si es año bisiesto
#Entradas
#   El año ingresado por el usuario
#Salida:
#   El mensaje final indica si el año es bisiesto
#Proceso
#   Se indica un año si el año es bisiesto arroja un mensaje "El año es bisiesto" sino aparece un mensaje "EL año no es bisiesto"

año = float(input("Ingrese el año"))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print (f"El {año} es bisiesto")
else:
    print (f"El {año} no es bisiesto")