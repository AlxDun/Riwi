print("Factorial de un número")
factorial=1
digito=int(input("Ingrese un digito: "))
for i in range (1,digito+1):
    factorial*=i
print("Factorial:", factorial)