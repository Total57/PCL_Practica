#Esteban Angeles Arriaga  -  Pensamiento Lógico Computacional  -  12/08/2024
# - - - - - - - - - CUENTO - - - - - - - - - 

name = input("Cual es tu nombre: ")


print(f"\nHola {name} .Aqui comienza tu travesia que estara llena de riesgos y recompensas.\n")

start = input("Estas seguro que quieres continuar si/no : ")

if start == "si":
    print(f"\nBien {name} aqui eres un joven aventurero que ha decidido explorar el misterioso Bosque Encantado. \nSe dice que en su interior hay criaturas mágicas y tesoros ocultos. \nUn día, armado con tu mochila y una linterna, te adentras en el bosque. \nDespués de caminar durante horas, llegas a una bifurcación en el camino.\n \n--------A la izquierda, el sendero parece más oscuro y cubierto de niebla.\n \n--------A la derecha, el camino está iluminado por la luz del sol que se filtra entre los árboles.\n")
    dec1 = input("\nCual camino eliges derecha o izquierda ( digita d/n ): ")

    if dec1 == "d":
        pass
    if dec1 == "i":
        
else:
    print("\nNo hay problema, hasta la próxima.")
