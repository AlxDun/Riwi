inventory={} # The dictionary where de products will be saved
def n(): print("\n") # Just a simple function to print a blank space
def fiveProducts(): # A function to add the first five products when the code is executed
    print("Ingrese los primeros 5 productos")
    while inventory.__len__()<5:
        name=input("Ingrese nombre del producto: ").lower()
        n()
        if name=="0": return
        elif name in inventory: return error(2), n()
        try:
            price=float(input("Ingrese precio del producto: "))
            n()
            while price<0:
                error(1)
                price=float(input("Ingrese precio del producto: "))
                n()
            amount=int(input("Ingrese cantidad del producto: "))
            n()
            while amount<=0:
                error(1)
                amount=float(input("Ingrese cantidad del producto: "))
                n()
            inventory[name]=[price, amount]
            print("El producto se ha añadido con exito."), n()
        except ValueError: n(), error(1), n()
def error(type): # Just a function to print common error messages
    if type==1: print("Ingrese un valor valido.")
    elif type==2: print("El producto ya existe.")
    elif type==3: print("El producto no existe.")
    elif type==4: print("El inventario está vacio.")
def menu(): print("1. Añadir productos al inventario."), print("2. Consultar productos del inventario."), print("3. Actualizar productos del inventario."), print("4. Eliminar productos del inventario."), print("5. Calcular valor total de los productos del inventario."), print("6. Salir."), n() # The menu with the options to the user, the user choose with numbers
def addProduct(): # The function where the user can add the products to the inventory with the name, the price and the amount
    while True:
        name=input("Ingrese nombre del producto (0 para volver al menú): ").lower()
        n()
        if name=="0": return
        elif name in inventory: return error(2), n()
        try:
            price=float(input("Ingrese precio del producto: "))
            n()
            while price<0:
                error(1)
                price=float(input("Ingrese precio del producto: "))
                n()
            amount=int(input("Ingrese cantidad del producto: "))
            n()
            while amount<=0:
                error(1)
                amount=float(input("Ingrese cantidad del producto: "))
                n()
            inventory[name]=[price, amount]
            print("El producto se ha añadido con exito."), n()
        except ValueError: n(), error(1), n()
def consultProduct(): # The function will display the products in the inventory to consult any of them just writing the name
    if inventory.__len__()==0: return error(4), n()
    while True:
        print("Lista de productos en el inventario:")
        for i in inventory.keys(): print(i)
        n()
        try:
            name=input("Ingrese el nombre del producto a consultar (0 para volver al menú): ").lower()
            if name=="0": return n()
            print(f"El precio es: ${inventory[name][0]}"), print(f"La cantidad es: {inventory[name][1]}"), n()
        except KeyError: n(), error(3), n()
def updateProduct(): # When the user wants to update a product just write the name and the new details of the product and then, the product will update
    if inventory.__len__()==0: return error(4), n()
    while True:
        print("Lista de productos en el inventario:")
        for i in inventory.keys(): print(i)
        n()
        name=input("Ingrese el nombre del producto a actualizar (0 para volver al menú): ").lower()
        n()
        if name=="0": return
        elif name not in inventory: return error(3), n()
        try:
            price=float(input("Ingrese el nuevo precio del producto: "))
            n()
            while price<0:
                error(1)
                price=float(input("Ingrese el nuevo precio del producto: "))
                n()
            amount=int(input("Ingrese la nueva cantidad del producto: "))
            n()
            while amount<=0:
                error(1)
                amount=float(input("Ingrese la nueva cantidad del producto: "))
                n()
            inventory[name]=[price, amount]
        except ValueError: n() ,error(1), n()
def removeProduct(): # The user just write a product name and the product will be deleted
    while True:
        if inventory.__len__()==0: return error(4), n()
        print("Lista de productos en el inventario:")
        for i in inventory.keys(): print(i)
        n()
        name=input("Ingrese el producto que desea eliminar (0 para volver al menú): ").lower()
        n()
        if name=="0": return
        if name not in inventory: error(3), n()
        for i in inventory.keys():
            if i==name:
                inventory.pop(name), print("El producto se ha eliminado con exito."), n()
                break
def calculateInventory(): # When the function is called, the inventory total is printed
    if inventory.__len__()==0: return error(4), n()
    total=0
    for i in inventory.values():
        productTotal=i[0]*i[1]
        total+=productTotal
    print(f"El total del inventario es: ${total}"), n()
print("Bienvenido al sitema de gestion de inventario."), n(), fiveProducts()
while True:
    menu() # The menu will be displayed everytime the user completes an action to choose the next one
    try:
        decision=int(input("Ingrese la opcion que desea: ")) # Here is where the user write the number to choose his action
        n()
        if decision==1: addProduct() # When the user write the number, the "decision" is validated by a series of conditionals and the function is called to execute the code
        elif decision==2: consultProduct()
        elif decision==3: updateProduct()
        elif decision==4: removeProduct()
        elif decision==5: calculateInventory()
        elif decision==6: # An additional option to finish the execution just breaking the main cicle
                print("Saliendo.")
                break
        else: error(1), n() # When the user choose an not allowed option a message of error is displayed
    except ValueError: n(), error(1), n()