
nombre = input("Hola cual es tu nombre: ")

print(f"Bienvenido a Cinepolis {nombre}, esta es nuestra cartlera de hoy:\n \n ------- Deadpool (A) ------- \n ------- Bettlejuice (B) ------- \n ------- Coraline (C) -------\n  ")

pelicula = input("Que pelicula deseas ver (Selecciona la letra asignada en paréntesis): ")

if pelicula == "A":
    edad = int(input(f"Buena elección {nombre}, ahora que edad tienes:"))

    if edad >= 18:
        pal = input(f"Que disfrutes tu película {nombre}, te gusatian una palomitas si/no: ")

        if pal == "si":
            print("Estos son los sabores: \n ------- Normal (A) ------- \n ------- Caramelo (B) ------- \n ------- Mantequilla (C) -------\n")
            sabor = input("Que sabor quiere (Selecciona la letra asignada en paréntesis): ")

            if sabor == "A":
                print(f"Bien {nombre} En un momento te llegan tus palomitas normales disfruta Deadpool 3 ")
            elif sabor == "B":
                print(f"Bien {nombre} En un momento te llegan tus palomitas con caramelo disfruta Deadpool 3")
            elif sabor == "C":
                print(f"Bien {nombre} En un momento te llegan tus palomitas con mantequilla disfruta lDeadpool 3")

            
        else:
            print("Perfecto disfruta tu película")
    else:
        print("Lo siento, eres menor de edad asi que no puedes ver esta película, ten un lindo día")


if pelicula == "B":
    int(input(f"Buena elección {nombre}, ahora que edad tienes:"))

    if edad >= 13:
        pal = input(f"Que disfrutes tu película {nombre}, te gusatian una palomitas si/no: ")

        if pal == "si":
            print("Estos son los sabores: \n ------- Normal (A) ------- \n ------- Caramelo (B) ------- \n ------- Mantequilla (C) -------\n")
            sabor = input("Que sabor quiere (Selecciona la letra asignada en paréntesis): ")

            if sabor == "A":
                print(f"Bien {nombre} En un momento te llegan tus palomitas normales disfruta Deadpool 3 ")
            elif sabor == "B":
                print(f"Bien {nombre} En un momento te llegan tus palomitas con caramelo disfruta Deadpool 3")
            elif sabor == "C":
                print(f"Bien {nombre} En un momento te llegan tus palomitas con mantequilla disfruta lDeadpool 3")

            
        else:
            print("Perfecto disfruta tu película")
    else:
        print("Lo siento, debes ser mayor de 13 años para verla , ten un lindo día")


if pelicula == "C":
    int(input(f"Buena elección {nombre}, ahora que edad tienes:"))

    if edad >= 18:
        pal = input(f"Que disfrutes tu película {nombre}, te gusatian una palomitas si/no: ")

        if pal == "si":
            print("Estos son los sabores: \n ------- Normal (A) ------- \n ------- Caramelo (B) ------- \n ------- Mantequilla (C) -------\n")
            sabor = input("Que sabor quiere (Selecciona la letra asignada en paréntesis): ")

            if sabor == "A":
                print(f"Bien {nombre} En un momento te llegan tus palomitas normales disfruta Deadpool 3 ")
            elif sabor == "B":
                print(f"Bien {nombre} En un momento te llegan tus palomitas con caramelo disfruta Deadpool 3")
            elif sabor == "C":
                print(f"Bien {nombre} En un momento te llegan tus palomitas con mantequilla disfruta lDeadpool 3")

            
        else:
            print("Perfecto disfruta Coralines")
    else:
        print("Lo siento, debes ser mayor a 5 años para ver esta película, ten un lindo día")



