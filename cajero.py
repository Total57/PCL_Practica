saldos = {"BBVA":15000, "Santander":18000, "Azteca":20000}
bancos = list(saldos.keys())


def sald(banco,saldo):
    print(f"\n----- Tu saldo con {banco} = ${saldo} -----")

def ret(saldo, banco, max):
    retiro = int(input("\nCuanto dinero deseas retirar: "))

    while retiro > saldo or retiro > max:
        
        retiro = int(input("\nNo puedes hacer un retiro que sea superior a tu saldo o a $9900 por favor intenta de nuevo: "))
    
    saldos[banco] = saldos[banco] - retiro

    print(f"\n----- Acabas de retirar ${retiro} -----")

def abono(banco):
    abono = int(input("\nCuanto dinero deseas abonar: "))

    saldos[banco] = saldos[banco] + abono

    print(f"\n----- Acabas de abonar ${abono} -----")

start = input("\nQuieres iniciar el cajero automático s/n: ")

while start == "s":
    start = start + "."

    print("\n--------- BANCOS ---------\n  1 - BBVA\n  2 - Santander\n  3 - Banco Azteca\n--------- BANCOS ---------\n")
    banco = input("Selecciona el banco que deseas ulitizar: ")

    if banco == "1" or banco == "BBVA":
        nip = "1234"

        pswd = input("Por favor digita tu nip: ")

        while pswd != nip:
            pswd = input("Tu nip es incorrecto intenta de nuevo: ")
        
        if pswd == nip:

            print("\n--------- BBVA ---------\n  1 - Consultar saldo\n  2 - Hacer un Retiro\n  3 - Hacer un abono\n  4 - Salir\n--------- BBVA ---------\n")
            modo = input("Selecionoa que acción deseas hacer: ")

            if modo == "1" or modo == "Consultar saldo":
                sald(bancos[0],saldos["BBVA"])
        
            if modo == "2" or modo == "Hacer un Retiro":
                ret(saldos["BBVA"], "BBVA", 9900)

            if modo == "3" or modo == "Hacer un abono":
                abono("BBVA")
    
    
    if banco == "2" or banco == "Santander":
        nip = "5678"

        pswd = input("Por favor digita tu nip: ")

        while pswd != nip:
            pswd = input("Tu nip es incorrecto intenta de nuevo: ")
        
        if pswd == nip:

            print("\n--------- Santander ---------\n  1 - Consultar saldo\n  2 - Hacer un Retiro\n  3 - Hacer un abono\n  4 - Salir\n--------- Santander ---------\n")
            modo = input("Selecionoa que acción deseas hacer: ")

            if modo == "1" or modo == "Consultar saldo":
                sald(bancos[1],saldos["Santander"])
        
            if modo == "2" or modo == "Hacer un Retiro":
                ret(saldos["Santander"], "Santander", 11000)

            if modo == "3" or modo == "Hacer un abono":
                abono("Santander")
    

    if banco == "3" or banco == "Banco Azteca":
        nip = "9876"

        pswd = input("Por favor digita tu nip: ")

        while pswd != nip:
            pswd = input("Tu nip es incorrecto intenta de nuevo: ")
        
        if pswd == nip:

            print("\n--------- Banco Azteca ---------\n  1 - Consultar saldo\n  2 - Hacer un Retiro\n  3 - Hacer un abono\n  4 - Salir\n--------- Banco Azteca ---------\n")
            modo = input("Selecionoa que acción deseas hacer: ")

            if modo == "1" or modo == "Consultar saldo":
                sald(bancos[2],saldos["Azteca"])
        
            if modo == "2" or modo == "Hacer un Retiro":
                ret(saldos["Azteca"], "Azteca", 10000)

            if modo == "3" or modo == "Hacer un abono":
                abono("Azteca")      
    
    start = input("\nQuieres hacer otra acción s/n: ")