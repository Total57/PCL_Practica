print("\nEste es un TRADUCTOR el cual es capaz de traducir solo COLORES a distintos idiomas. A continuacipon el menú: ")
print("\n-----------MENÚ-----------\n   Español a Inglés - 1\n   Inglés a Español - 2\n-----------MENÚ-----------\n")

colores = ["rojo", "naranja", "amarrillo", "verde", "morado", "azul", "rosa", "blanco", "negro", "cafe"]
colors = ["red", "orange", "yellow", "green", "purple", "blue", "pink", "white", "black", "brown"]

modos = ["1", "2",]

modo = str(input("Escribe el digito relacionado al modo de traducción que dessea usar: "))

while modo not in modos:
    modo = input("Ecribe un digito con un modo existente: ")

if modo == "1":
    print("\n---------ESPAÑOL a INGLÉS---------")
    word = input("Escribe el color en español, en minúsculas y sin acentos: ")

    while word not in colores:
        if word in colors:
            word = input("Ese ya es un color en inglés por favor escribe uno en español: ")
        else:
            word = input("No conocemos ese color, por favor escribe otro: ")

    if word == colores[0]:
        print(f"\n----- {colores[0]} = {colors[0]} ----\n")
    elif word == colores[1]:
        print(f"\n----- {colores[1]} = {colors[1]} ----\n")
    elif word == colores[2]:
        print(f"\n----- {colores[2]} = {colors[2]} ----\n")
    elif word == colores[3]:
        print(f"\n----- {colores[3]} = {colors[3]} ----\n")
    elif word == colores[4]:
        print(f"\n----- {colores[4]} = {colors[4]} ----\n")
    elif word == colores[5]:
        print(f"\n----- {colores[5]} = {colors[5]} ----\n")
    elif word == colores[6]:
        print(f"\n----- {colores[6]} = {colors[6]} ----\n")
    elif word == colores[7]:
        print(f"\n----- {colores[7]} = {colors[7]} ----\n")
    elif word == colores[8]:
        print(f"\n----- {colores[8]} = {colors[8]} ----\n")
    elif word == colores[9]:
        print(f"\n----- {colores[9]} = {colors[9]} ----\n")
    elif word == colores[10]:
        print(f"\n----- {colores[10]} = {colors[10]} ----\n")
        
if modo == "2":

    print("\n---------INGLÉS a ESPAÑOL---------")
    word = input("Escribe el color en inglés y en minúsculas : ")

    while word not in colors:
        if word in colores:
            word = input("Ese ya es un color en español por favor escribe uno en inglés: ")
        else:
            word = input("No conocemos ese color, por favor escribe otro: ")

    if word == colors[0]:
        print(f"\n----- {colors[0]} = {colores[0]} ----\n")
    elif word == colors[1]:
        print(f"\n----- {colors[1]} = {colores[1]} ----\n")
    elif word == colors[2]:
        print(f"\n----- {colors[2]} = {colores[2]} ----\n")
    elif word == colors[3]:
        print(f"\n----- {colors[3]} = {colores[3]} ----\n")
    elif word == colors[4]:
        print(f"\n----- {colors[4]} = {colores[4]} ----\n")
    elif word == colors[5]:
        print(f"\n----- {colors[5]} = {colores[5]} ----\n")
    elif word == colors[6]:
        print(f"\n----- {colors[6]} = {colores[6]} ----\n")
    elif word == colors[7]:
        print(f"\n----- {colors[7]} = {colores[7]} ----\n")
    elif word == colors[8]:
        print(f"\n----- {colors[8]} = {colores[8]} ----\n")
    elif word == colors[9]:
        print(f"\n----- {colors[9]} = {colores[9]} ----\n")
    elif word == colors[10]:
        print(f"\n----- {colors[10]} = {colores[10]} ----\n")
