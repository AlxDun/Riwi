print("Número primo")
divisores=0
numero=int(input("Ingrese un numero: "))
for i in range (1, numero+1):
    residuo=numero%i
    if residuo==0:
        divisores+=1
if divisores==2:
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo")