print("Validar una contraseña")
contraseña="Qwe.123*"
intento=""
while contraseña!=intento:
    intento=str(input("Ingrese la contraseña: "))
    if contraseña==intento: break
    print("Contraseña incorrecta")
print("Contraseña correcta")