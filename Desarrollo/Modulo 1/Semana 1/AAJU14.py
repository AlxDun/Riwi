print("Suma de números hasta ingresar 0")
sumatoria=0
digito=int(input("Ingrese un digito: "))
while digito!=0:
    sumatoria=sumatoria+digito
    digito=int(input("Ingrese un digito: "))
print("Sumatoria:", sumatoria)