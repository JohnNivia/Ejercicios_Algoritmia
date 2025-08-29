#Nombre: Se verifica si la temperatura esta apta para congelar
#Entrada:
#   Se indica la temperatura 
#Salida:
#   Si la temperatura es negativa aparece un mensaje
#Proceso:
#   Se indica la temperatura, si es negativa aparece un mensaje 
temperatura = float (input ("Ingrese la temperatura "))
if temperatura <= 0:
    print ("Esta apto para congelar")
else:
    print ("No esta apto para congelar")