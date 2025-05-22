print("Factorial de un número.")
factorial=1
numero=int(input("Ingrese un numero: "))
for i in range (1, numero+1):
    factorial*=i
print(f"Factorial: {factorial}")