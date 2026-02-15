# Programa que calcula el promedio de 3 números

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3

# BUG: división incorrecta
promedio = suma / 2

# Prints de debug
print("DEBUG -> Suma:", suma)
print("DEBUG -> Promedio calculado:", promedio)

print("El promedio es:", promedio)
