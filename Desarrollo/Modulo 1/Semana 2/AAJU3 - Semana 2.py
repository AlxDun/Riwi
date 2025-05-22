print("Suma de los primeros n números")
sumatoria=0
numero=int(input("Ingrese un numero: "))
for i in range (0, numero+1):
    sumatoria+=i
print(f"Sumatoria: {sumatoria}")