print("Suma de números hasta que el usuario diga basta")
sumatoria=0
while True:
    entrada=input("Ingrese un numero: ")
    if entrada=="basta":
        break
    numero=int(entrada)
    sumatoria+=numero
print(f"Sumatoria: {sumatoria}")