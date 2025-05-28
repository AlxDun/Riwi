print("Número positivo o negativo")
while True:
    try:
        numero=int(input("Ingrese un numero: "))
        if numero<0:
            print("el numero es negativo.")
        elif numero>0:
            print("El numero es positivo.")
        else:
            print("El numero es 0.")
    except ValueError:
        print("Solo se aceptan numeros.")
        break