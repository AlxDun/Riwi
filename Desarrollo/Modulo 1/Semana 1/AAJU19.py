#print("Mostrar los primeros N números pares")
digito=int(input("Ingrese un digito: "))
for i in range (1, digito+1):
    residuo=i%2
    if residuo==0:
        print(i)