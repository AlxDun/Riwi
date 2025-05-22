print("Verificar si un número es par o impar")
numero=int(input("Escriba el digito: "))
residuo=numero%2
if residuo==1: print("El numero", numero, "es impar")
else: print("El numero", numero, "es par")