print("Piramide de números.")
numero=int(input("Ingrese el numero de filas: "))
for i in range (1, numero+1):
    eslabon=""
    for j in range (1, i+1):
        eslabon+=str(j)
    print(eslabon)