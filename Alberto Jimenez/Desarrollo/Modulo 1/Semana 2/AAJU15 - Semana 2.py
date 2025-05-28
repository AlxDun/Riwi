print("Matriz de ceros y unos alternados.")
for filas in range(5):
    binario=""
    for columnas in range(5):
        if (filas+columnas)%2==0:
            binario+="0 "
        else:
            binario+="1 "
    print(binario)