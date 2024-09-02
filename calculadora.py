import math 

start = input("\n¿Desea iniciar la calculadora? s/n: ")
modos = ["1", "2", "3", "4", "5", "6"]

def suma():
    print("\n-----SUMA-----\n")
    num1 = float(input("Digite el primer sumando: "))
    num2 = float(input("Digite el segundo sumando: "))
    resultado = num1 + num2
    print(f"\n----- {num1} + {num2} = {resultado} -----")

def resta():
    print("\n-----RESTA-----\n")
    num1 = float(input("Digite el minuendo: "))
    num2 = float(input("Digite el sustraendo: "))
    resultado = num1 - num2
    print(f"\n----- {num1} - {num2} = {resultado} -----")

def mult():
    print("\n-----MULTIPLICACIÓN-----\n")
    num1 = float(input("Digite el primer factor: "))
    num2 = float(input("Digite el primer segundo: "))
    resultado = num1 * num2
    print(f"\n----- {num1} x {num2} = {resultado} -----")

def div():
    print("\n-----DIVISIÓN-----\n")
    num1 = float(input("Digite el dividendo: "))
    num2 = float(input("Digite el divisor: "))
    resultado = num1 / num2
    print(f"\n----- {num1} / {num2} = {resultado} -----")

def pot():
    print("\n-----POTENCIA-----\n")
    num1 = float(input("Digite la base de la potencia: "))
    num2 = float(input("Digite el exponente: "))
    resultado = num1 ** num2
    print(f"\n----- {num1} elevado a {num2} = {resultado} -----")

def raiz():
    print("\n-----RAÍZ CUADRADA-----\n")
    num = float(input("Digite el numero para sacarle la raíz cuadrada: "))
    resultado = math.sqrt(num)
    print(f"\n----- La raíz cuadrada de {num} = {resultado} -----")

while start == "s":
    start = "s" + "."
    print("\n------MENU------\n1 - SUMA\n2 - RESTA\n3 - MULTIPLICACIÓN\n4 - DIVISIÓN\n5 - Potencia\n6 - Raíz Cuadrada\n------MENU------")
    
    modo = input("\nSeleciona un modo: ")

    while modo not in modos:
        modo = input("Por favor digite una opción válida: ")

    if (modo == "1"):
        suma()

    if (modo == "2"):
        resta()

    if (modo == "3"):
        mult()

    if (modo == "4"):
        div()
    
    if (modo == "5"):
        pot()

    if (modo == "6"):
        raiz()

    start = input("\n¿Desea hacer otra operación? s/n: ")

print("---------FIN---------")