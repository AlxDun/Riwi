print("Menú interactivo.")
print("1 para sumar.")
print("2 para restar.")
print("3 para salir.")
while True:
    opcion=int(input("Ingrese su opcion: "))
    if opcion==1:
        numero1=int(input("Ingrese el primer digito: "))
        numero2=int(input("Ingrese el segundo digito: "))
        print(f"{numero1} + {numero2} = {numero1+numero2}")
        break
    elif opcion==2:
        numero1=int(input("Ingrese el primer digito: "))
        numero2=int(input("Ingrese el segundo digito: "))
        print(f"{numero1} - {numero2} = {numero1-numero2}")
        break
    elif opcion==3:
        print("Saliendo")
        break
    else:
        print("ingrese una opcion valida.")