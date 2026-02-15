# Programa que calcula el promedio de 3 números

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3

# Correccion del bug:
promedio = suma / 3

print("El promedio es:", promedio)
