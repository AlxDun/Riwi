# Un simple titulo
print("Tienda de Alberto")
print("\n")

# Declaracion de variables globales
producto=""
cantidad=1
info="no"

# Inicio de la compra
print("¡Bienvenido a la tienda de Alberto!")
compra=str(input("¿Desea realizar una compra? (si/no) "))
if compra=="si":

    # Una simple bienvenida 
    print("\n")
    print("¡Buenas tardes!")

    # Ciclo para validar informacion
    while info=="no":

        # Nombre del producto
        producto=str(input("¿Que producto desea comprar? "))
        while producto=="":
            print("\n")
            print("Debe ingresar un producto valido")
            producto=str(input("¿Que producto desea comprar? "))

        # Precio unitario
        print("\n")
        precio=float(input("¿Cuanto cuesta el producto que desea comprar? "))

        # Cantidad de productos adquiridos
        print("\n")
        a=str(input("¿Desea comprar mas de un producto? (si/no) "))
        if a=="si":
            print("\n")
            cantidad=int(input("¿Cuantos productos desea comprar? "))
            while cantidad<=1:
                print("\n")
                print("Debe ingresar una cantidad valida.")
                cantidad=int(input("¿Cuantos productos desea comprar? "))

        # El porcentaje de descuento que se aplicará
        print("\n")
        b=str(input("¿Tiene un descuento que aplicar? (si/no) "))
        if b=="si":
            print("\n")
            descuento=float(input("¿De cuanto es su descuento? "))
            while descuento<0 or descuento>100:
                print("\n")
                print("Ingrese un descuento valido")
                descuento=float(input("¿De cuanto es su descuento? "))

        # Informacion final
        print("\n")
        print("¡Muy bien! Aqui está la informacion de su pedido.")
        print("\n")
        print("Nombre del producto:", producto)
        print("Precio del producto individual: $", precio)

        # La cantidad solo se muestra si se compra mas de un producto
        if a=="si":
            print("Cantidad del producto:", cantidad)

        # El descuento solo se muestra si se le aplica uno
        if b=="si":
            descuentoDecimal=descuento/100
            print("Precio final sin descuento: $", precio*cantidad)
            print(f"Descuento a aplicar: {descuento}%")
            print("Precio final con descuento: $", (precio*cantidad)*(1-descuentoDecimal))
        else:
            print("No se aplica ningun descuento")
            print("Precio final: $", precio*cantidad)

        print("\n")
        info=str(input("¿Su informacion es correcta? (si/no) "))
        print("\n")
    print("¡Su compra fue exitosa!")

else:
    print("\n")
    print("¡Que tenga buena tarde!")