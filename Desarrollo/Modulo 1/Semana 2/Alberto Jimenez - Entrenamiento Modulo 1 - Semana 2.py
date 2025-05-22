#Un titulo
print("Calificaciones y estadisticas.")
print("\n")

#declaracion de la lista de calificaciones
notas=[]

#Una funcion para imprimir el menú con un solo comando
def menu():
    print("1 Determinar el estado de aprobación.")
    print("2 Calcular el promedio.")
    print("3 Contar calificaciones mayores.")
    print("4 Verificar y contar calificaciones específicas.")
    print("5 Agregar calificaciones a la lista.")
    print("6 Limpiar la lista.")
    print("7 Ver lista.")
    print("0 Salir.")

#Todo el codigo en un bucle para que se repita indefinidamente hasta que el usiario decida salir
while True:
    try:

        #Se imprime el menú
        menu()

        #El usuario decide que desea hacer
        opcion=int(input("¿Que opcion desea? "))
        print("\n")

        #Si selecciona la opcion 1, se ejecuta el codigo de la opcion 1
        if opcion==1:
            while True:
                try:

                    #Pide el numero a verificar
                    calificacion=int(input("Ingrese calificacion (entre 0 y 100): "))

                    #Sigue pidiendo un numero hasta que esté dentro de los parametros
                    while calificacion<0 or calificacion>100:
                        print("Ingrese un valor valido.")
                        print("\n")
                        calificacion=int(input("Ingrese calificacion (entre 0 y 100): "))

                    #Si el numero es menor a 51, está reprobado
                    if calificacion<51:
                        print("Reprobado.")
                        print("\n")
                        break

                    #Si no es menor, significa que es mayor y está aprobado
                    else:
                        print("Aprobado.")
                        print("\n")
                        break

                #Por si el usuario digita algo que no sea un numero
                except ValueError:
                    print("Ingrese una calificacion valida.")
                    print("\n")

        #Si selecciona la opcion 2, se ejecuta el codigo de la opcion 2
        elif opcion==2:
            while True:
                try:

                    #Pido los numeros separados por comas y los guardo como una cadena
                    notaCadena=input("Ingresa las calificaciones separadas por comas (entre 0 y 100): ")

                    #Recorro toda la cadena, la divido por las comas y le elimino los espacios vacios para guardarlos en la lista como cadenas
                    listaNotaCadena=[i.strip() for i in notaCadena.split(",")]

                    #Declaro la lista que voy a usar para almacenar los numeros ya como un float
                    lista=[]

                    #Recorro toda la lista de cadenas y las convierto en float para guardarlos en la lista, si no se pueden transformar en float o no cumplen con los parametros, se omiten
                    for i in listaNotaCadena:
                        try:
                            nota=float(i)
                            if nota<0 or nota>100:
                                continue
                            else:
                                lista.append(nota)
                        except ValueError:
                            continue

                    #Se calcula e imprime el promedio
                    promedio=sum(lista)/len(lista)
                    print(f"El promedio de las calificaciones es: {promedio:.3f}")
                    print("\n")
                    break

                #Si la lista se encuentra vacia se reinicia el ciclo y vuelve a pedir los numeros
                except ZeroDivisionError:
                    print("Ingrese valores validos.")
                    print("\n")

        #Si selecciona la opcion 3, se ejecuta el codigo de la opcion 3
        elif opcion==3:
            while True:

                #Si la lista se encuentra vacia, se rompe el ciclo y le sugiere al usuario ir a la opcion 5 para llenar la lista
                if len(notas)==0:
                    print("La lista esta vacia, primero llenela en la opcion 5.")
                    print("\n")
                    break
                try:

                    #Declaro el contador que va a ser la cantidad de notas mayores a la que el usuario digite
                    contador=0

                    #Pido el numero a comparar a el usuario
                    comparar=int(input("Ingrese el valor a comparar (entre 0 y 100): "))

                    #Un ciclo para que solo continue si el numero digitado por el usuario está dentro de los parametros
                    while comparar<0 or comparar>100:
                        print("Ingrese un valor valido.")
                        print("\n")
                        comparar=int(input("Ingrese el valor a comparar (entre 0 y 100): "))
                    
                    #Recorro la lista de notas y se salta las que son menores al numero digitado, si no, significa que es mayor y se le suma 1 al contador
                    for i in notas:
                        if i<=comparar:
                            continue
                        else:
                            contador+=1
                    
                    #Se imprimen cuantas notas son mayores al numero que digita el usuario
                    print(f"Hay {contador} calificaciones mayores a {comparar} en la lista.")
                    print("\n")
                    break

                #Excepcion por si el valor digitado por el usuario no es valido
                except ValueError:
                    print("Ingrese un valor valido.")
                    print("\n")

        #Si selecciona la opcion 4, se ejecuta el codigo de la opcion 4
        elif opcion==4:
            while True:
                #Si la lista se encuentra vacia, se rompe el ciclo y le sugiere al usuario ir a la opcion 5 para llenar la lista
                if len(notas)==0:
                        print("La lista esta vacia, primero llenela en la opcion 5.")
                        print("\n")
                        break
                try:

                    #Declaro el contador que va a ser la cantidad de notas mayores a la que el usuario digite
                    contador=0

                    #Pido el numero a contar a el usuario
                    iguales=int(input("Ingese el valor a contar (entre 0 y 100): "))

                    #Un ciclo para que solo continue si el numero digitado por el usuario está dentro de los parametros
                    while iguales<0 or iguales>100:
                        print("Ingrese un valor valido.")
                        print("\n")
                        iguales=int(input("Ingrese el valor a contar (entre 0 y 100): "))

                    #Recorro la lista de notas y si la iteracion es igual a el numero digitado, se le suma 1 al contador
                    for i in notas:
                        if i==iguales:
                            contador+=1

                    #Se imprimen cuantas notas son iguales al numero que digita el usuario
                    print(f"Hay {contador} calificaciones iguales a {iguales} en la lista.")
                    print("\n")
                    break

                #Excepcion por si el valor digitado por el usuario no es valido
                except ValueError:
                    print("Ingrese un valor valido.")
                    print("\n")

        #Si selecciona la opcion 5, se ejecuta el codigo de la opcion 5
        elif opcion==5:
            while True:

                #Pido los numeros separados por comas y los guardo como una cadena
                notaCadena=input("Ingresa las calificaciones separadas por comas (entre 0 y 100): ")

                #Recorro toda la cadena, la divido por las comas y le elimino los espacios vacios para guardarlos en la lista como cadenas
                listaNotaCadena=[i.strip() for i in notaCadena.split(",")]

                #Recorro toda la lista de cadenas y las convierto en float para guardarlos en la lista, si no se pueden transformar en float o no cumplen con los parametros, se omiten
                for i in listaNotaCadena:
                    try:
                        nota=float(i)
                        if nota<0 or nota>100:
                            continue
                        else:
                            notas.append(nota)
                    except ValueError:
                        continue

                #Si el usuario ingresa al menos un valor valido, se añade a la lista, si no es el caso, vuelve a pedir los valores
                if len(notas)>0:
                    print("Se añadieron correctamente a la lista los valores validos.")
                    print("\n")
                    break
                else:
                    print("Ingrese valores validos.")
                    print("\n")
        
        #Si selecciona la opcion 6, se ejecuta el codigo de la opcion 6
        elif opcion==6:
            while True:

                #Si la lista se encuentra vacia, se rompe el ciclo y le sugiere al usuario ir a la opcion 5 para llenar la lista
                if len(notas)==0:
                    print("La lista esta vacia, primero llenela en la opcion 5.")
                    print("\n")
                    break

                #Si el usuario esta seguro de vaciar la lista solo se vacia y listo, de lo contrario, se despliega de nuevo el menú
                print("¿Esta seguro que desea vaciar la lista?")
                vaciar=input("si/no: ")
                if vaciar.lower()=="si":
                    notas.clear()
                    print("La lista se ha vaciado.")
                    print("\n")
                    break
                elif vaciar.lower()=="no":
                    print("Cancelando.")
                    print("\n")
                    break

                #Si el usuario no escoge una de las dos opciones, vuelve a pedir que ingrese su desicion
                else:
                    print("Ingrese una opcion valida.")
                    print("\n")

        #Si selecciona la opcion 7, se muestra la lista si esta contiene algun elemento, de lo contrario, se le indicará al usuario que la lista está vacia y deberia llenarla
        elif opcion==7:
            if len(notas)==0:
                    print("La lista esta vacia, primero llenela en la opcion 5.")
                    print("\n")
            else:
                print(f"Lista: {notas}")
                print("\n")

        #Si selecciona la opcion 0, se cierra el programa
        elif opcion==0:
            print("Saliendo.")
            break

        #Si el usuario no selecciona una opcion valida
        else:
            print("Ingrese una opcion valida.")
            print("\n")
    
    #Si el usuario no selecciona un numero
    except ValueError:
        print("\n")
        print("Ingrese un valor valido.")
        print("\n")