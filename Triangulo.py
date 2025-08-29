#Nombre: Clasificación de triángulos por sus lados
#Entradas
#   Tres valores numéricos que representan los lados del triángulo
#Salida:
#   Un mensaje indicando si el triángulo es equilátero, isósceles o escaleno
#Proceso
#   Si los tres lados son iguales → equilátero,Si solo dos lados son iguales → isósceles y Si los tres lados son diferentes → escaleno
lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))

if lado1 == lado2 ==  lado3:
    print("El triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("EL triangulo es isoceles ")
else:
    print("El triangulo es escalano")
