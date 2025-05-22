print("Sumar solo los impares entre dos números.")
sumatoria=0
numero1=int(input("Ingrese el inicio: "))
numero2=int(input("Ingrese el final: "))
for i in range (numero1, numero2+1):
    if i%2==1:
        sumatoria+=i
print(f"La sumatoria de los numeros impares entre {numero1} y {numero2} es: {sumatoria}")