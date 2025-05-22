print("Buenas tardes, bienvenido a TechnoStore")
recaudo=float(0)
regalos=0
clientes=0
while True:
    nombre=str(input("Ingrese su nombre: "))
    if nombre=="fin":
        break
    cantidad=int(input("Cuantos productos desea: "))
    precio=int(input("Ingrese el precio unitario: "))
    pedido=precio*cantidad
    if cantidad>10:
        regalos+=1
        pedido*=0.9
    elif cantidad>=5:
        pedido*=0.9
    recaudo+=pedido
    clientes+=1
print(f"recaudo: ${recaudo}")
print(f"regalos: {regalos}")
print(f"clientes atendidos: {clientes}")