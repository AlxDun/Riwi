products={}
code=0
sales=[]
saleID=0
def error(type):
    if type==1:
        print("Ingrese un valor valido.")
    elif type==2:
        print("El producto no existe")
def addProduct():
    global code
    code+=1
    name=input("Ingrese el nombre del producto: ")
    try:
        price=float(input("Ingrese el precio del producto: "))
        category=input("Ingrese la categoría del producto: ")
        products[code]=(name, price, category)
    except ValueError:
        error(1)
def addSale():
    global saleID
    purchasedProducts=[]
    totalSale=0
    saleID+=1
    clientID=input("Ingrese nombre del cliente: ")
    try:
        product=int(input("Ingrese ID del producto a comprar (0 para finalizar): "))
        while product!=0:   
            totalSale+=products[product][1]
            purchasedProducts.append(products.pop(product))
            product=int(input("Ingrese ID del producto a comprar (0 para finalizar): "))
        sales.append((saleID, clientID, purchasedProducts, totalSale))
    except ValueError:
        error(1)
    except KeyError:
        error(2)
def consultProducts():
    for x in products:
        print(f"ID: {x} Nombre: {products[x][0]} Precio: {products[x][1]} Categoría: {products[x][2]}")
def consultClient():
    client=input("Ingrese nombre del cliente: ")
    for x in sales:
        if x[1]==client:
            print(x)
def consultCategory():
    category=input("Ingrese categoria: ")
    for x in products:
        if category==products[x][2]:
            print(x)
while True:
    desicion=int(input("Que opcion desea? "))
    if desicion==1:
        while True:
            addProduct()
            break
    if desicion==2:
        while True:
            addSale()
            break
    if desicion==3:
        while True:
            consultProducts()
            break
    if desicion==4:
        while True:
            consultClient()
            break
    if desicion==5:
        while True:
            consultCategory()
            break
    