import random 
numero_secreto = random .randint(1, 100)
intentos = 0
max_intentos = 7

while intentos < max_intentos:
    intento = int(input("Adivina (1_100): "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto, intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el numero en {intentos} intentos.")
        break
else:    
    print(f"Lo siento, has agotado tus intentos. El numero secreto era {numero_secreto}.") 