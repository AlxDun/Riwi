print("Adivina el número")
import random
numeroAlAzar=random.randint(0, 100)
print(numeroAlAzar)
numero=int(input("Ingrese un numero: "))
while True:
    if numero<numeroAlAzar:
        print("El numero es mayor.")
        numero=int(input("Ingrese un numero: "))
    elif numero>numeroAlAzar:
        print("El numero es menor.")
        numero=int(input("Ingrese un numero: "))
    else:
        print(f"Adivinaste, el numero era: {numeroAlAzar}")
        break