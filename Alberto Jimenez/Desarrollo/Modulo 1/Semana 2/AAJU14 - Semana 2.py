print("Números primos entre 1 y 100.")
for numero in range(2, 101):
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero)