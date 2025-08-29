#Nombre: Programa para obtener iniciales en mayuscula
#Entradas: 
#   Variable y función ,
#   Variable y función
#Salidas:
#   Iniciales: Las primeras letras de nombre y apellido
#Proceso:
#   Pide el nombre de la persona y extrae la primera letra del nombre y apellido y inprime las iniciales


#Pedir nombre y apellido
Nombre = input ("Ingrese su nombre: "),
Apellido =input("Ingrese su apellido: ")

# Tomar la primera letra de cada uno y ponerla en mayúscula
Iniciales = Nombre[0].upper() + Apellido[0].upper()

#Mostrar el resultado
print("Tus iniciales son:", Iniciales)