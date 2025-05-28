print("Adivina el número")
vocales=0
palabra=str(input("Ingrese una palabra: "))
for palabras in palabra:
    if palabras=="a" or palabras=="e" or palabras=="i" or palabras=="o" or palabras=="u":
        vocales+=1
print(f"Hay {vocales} vocales en la palabra {palabra}.")