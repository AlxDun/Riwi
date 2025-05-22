print("Dibujar un rectángulo con caracteres.")
alto=int(input("Ingrese el alto: "))
ancho=int(input("Ingrese el ancho: "))
for i in range (alto):
    for j in range (ancho):
        print("*", end="")
    print()