# Un simple titulo
print("Gestion de inventario")

# Declaracion de el diccionario donde se van a guardar los productos
products={"guineo":{"precio": 500.0, "cantidad": 5}}

# Decalaro la funcion lambda para multiplicar facilmente
multiply=lambda a, b: a*b

# Funcion que se ejecutará cuando el usuario digite un valor no valido
def error():
    print("Ingrese valor valido.")
    print("\n")

# Menu que se imprimirá cada que el usuario requiera hacer alguna otra accion
def menu():
    print("1 Añadir producto.")
    print("2 Consultar producto.")
    print("3 Actualizar producto.")
    print("4 Eliminar producto.")
    print("5 Calcular valor total de productos.")
    print("6 Salir.")
    print("\n")

# Funcion en la que se añadiran los productos al diccionario
def addProduct():

    #Pido el nombre de el producto que desea guardar
    name=input("Ingrese nombre del producto: ").strip().lower()
    print("\n")

    # Condicional que valida si el producto que el usuario intenta registrar ya existe
    if name in products:
        print("El producto ya existe.")
        print("\n")
        return
    
    # Ciclo que se repetirá cada vez que el usuario coloque un valor invalido
    while True:
        try:
            price=float(input("Ingrese el precio del producto: "))
            print("\n")

            # Pequeño ciclo que se ejecuta si el valor es menor a 0
            while price<0:
                error()
                price=float(input("Ingrese el precio del producto: "))
                print("\n")

            amount=int(input("Ingrese la cantidad del producto: "))
            print("\n")
            while amount<0:
                error()
                amount=int(input("Ingrese la cantidad del producto: "))
                print("\n")

            # El producto se guarda en el diccionario, el nombre de el producto es la clave y el precio junto con la cantidad se guardan en otro diccionario anidado con sus propias claves correspondientes
            products[name]={"price": price, "amount": amount}

            # Se le notifica al usuario que el producto se añadio correctamente
            print(f"Producto {name} añadido correctamente.")
            print("\n")
            break

        # Excepcion que se ejecuta cuando el usuario ingresa un valor invalido
        except ValueError:
            print("\n")
            error()

# Funcion que se ejecuta cuando el usuario quiere consultar los productos del inventario
def consultProduct():

    # Condicional que valida si el diccionario está vacio
    if products.__len__()==0:
        print("No hay productos.")
        print("\n")
        return
    
    # Se imprimen los productos que ya se encuentran en el inventario
    print("Productos disponibles:")
    for x in products.keys():
        print(x)
    print("\n")
    try:

        # Pido el nombre del producto a consultar
        name=input("Ingrese nombre del producto: ").strip().lower()
        print("\n")

        # Se imprime el precio y la cantidad de el producto consultado
        print("Precio: $", products[name]["price"])
        print("Cantidad:", products[name]["amount"])
        print("\n")

    # Una excepcion que se ejecuta, cuando el producto no ha sido registrado
    except KeyError:
        print("El producto no existe.")
        print("\n")

# Funcion que se ejecuta cuando el usuario desea actualizar un producto
def updateProduct():

    # Condicional que valida si el diccionario está vacio
    if products.__len__()==0:
        print("No hay productos.")
        print("\n")
        return
    # Se imprimen los productos que ya se encuentran en el inventario
    print("Productos disponibles:")
    for x in products.keys():
        print(x)
    print("\n")
    try:

        # Pido el nombre del producto a actualizar
        name=input("Ingrese nombre del producto: ").strip().lower()
        print("\n")

        # Valida si el producto existe dentro de el inventario
        if products[name]:
            while True:
                try:

                    # Vuelvo a pedir los datos por los cuales se va a actualizar el producto cuidando que no ingrese un valor invalido
                    price=float(input("Ingrese el precio del producto: "))
                    print("\n")
                    while price<0:
                        error()
                        price=float(input("Ingrese la cantidad del producto: "))
                        print("\n")

                    amount=int(input("Ingrese la cantidad del producto: "))
                    print("\n")
                    while amount<0:
                        error()
                        amount=int(input("Ingrese la cantidad del producto: "))
                        print("\n")

                    # El producto se actualiza
                    products[name]={"price": price, "amount": amount}

                    # Se le notifica al usuario que el producto se actualizó correctamente
                    print(f"Producto {name} actualizado correctamente.")
                    print("\n")
                    break

                # Excepcion que se ejecuta cuando el usuario ingresa una valor invalido
                except ValueError:
                    print("\n")
                    error()
    
    # Excepcion que salta cuanto el producto que el usuario quiere actualizar no existe
    except KeyError:
        print("El producto no existe.")
        print("\n")

# Funcion que se ejecuta cuando el usuario quiere eliminar un producto
def deleteProduct():
    if products.__len__()==0:
        print("No hay productos.")
        print("\n")
        return
    # Se imprimen los productos que ya se encuentran en el inventario
    print("Productos disponibles:")
    for x in products.keys():
        print(x)
    print("\n")
    try:

        # Pido el nombre de el producto que el usuario desea eliminar
        name=input("Ingrese nombre del producto: ").strip().lower()

        # El producto se elimina con un .pop y se le notifica al usuario
        products.pop(name)
        print(f"El producto {name} se elimino correctamente.")
        print("\n")

    # Excepcion para cuando el producto no existe
    except KeyError:
        print("El producto no existe.")
        print("\n")

# Funcion que se ejecuta cuando se quiere calcular el valor total de todo el inventario
def calculateTotalProducts():

    # Declaro la variable en la que se almacenaria el total
    summation=0

    # Se usan unos ciclos anidados para iterar sobre los productos de el inventario y los valores que son el precio y la cantidad
    for x in products:
        for y in products[x].values():

            # Los valores se filtran y se almacenan en las variables que se utilizaran para hacer el calculo
            if type(y) is float:
                price=y
            elif type(y) is int:
                amount=y
        
        # Se realiza el calculo correspondiente y se va guardando en la variable que almacena el total
        summation+=multiply(price, amount)

    # Si la sumatoria es 0, significa que el inventario está vacio
    if summation==0:
        print("El inventario está vacio.")
        print("\n")

    # De lo contrario, se imprime el valor total de el inventario
    else:
        print(f"El valor total del inventario es: ${summation}")
        print("\n")

# Ciclo en el que se encontrará el usuario desde que ejecuta el programa hasta que decide salir
while True:

    # Se le guia al usuario por medio de un menu con diferentes opciones en la cual se accede digitando el valor correspondiente a la funcion deseada
    menu()
    try:

        # Se le pregunta al usuario que funcion del programa desea utilizar
        decision=int(input("Que opcion desea? "))
        print("\n")

        # Si el usuario coloca 1, se ejecuta la funcion correspondiente
        if decision==1:
            # Ciclo en el que el usuario ingrese con cada opcion cuidando que digite bien los valores cuando se ejecuten las susodichas
            while True:
                addProduct()
                # El ciclo se rompe cuando la funcion se completa con exito
                break
    
        # Si el usuario coloca 2, se ejecuta la funcion correspondiente y asi susesivamente con cada una de las funciones mostradas en el menu
        elif decision==2:
            while True:
                consultProduct()
                break

        elif decision==3:
            while True:
                updateProduct()
                break

        elif decision==4:
            while True:
                deleteProduct()
                break

        elif decision==5:
            while True:
                calculateTotalProducts()
                break
        
        # Si el usuario digita 6, el programa se cierra rompiendo el ciclo en el que se encuentra el usuario
        elif decision==6:
            print("Saliendo.")
            break
        
        # Si el usuario no digita ninguna de las opciones que el programa ofrece, se le notifica que esta digitando un valor invalido
        else:
            print("\n")
            error()

    # Excepcio que salta cuando el usuario digita un valor invalido difenrente a un numero
    except ValueError:
        print("\n")
        error()