bancos = ["BBVA", "Santander", "Banco Azteca"]

start = input("Bienvenido a Uber Eats, te gustaria ordenar algo de comida si/no: ")
cuenta = 0
porc = 0

while start == "si" or start == "Si" or start == "SI":
    start = start + "."
    print("\n-------------- MENU --------------\n 1 - Carnes\n 2 - Mariscos\n 3 - Pastas\n 4 - Bebidas\n 5 - Postres\n-------------- MENU --------------")
    modo = input("\nSelecciona el número dependo de lo que desea ordenar : ")

    if modo == "1":
        precios = {"Lomo": 450, "Costillas": 1000, "Res": 400, "Rib Eye": 550, "New York":1000}
        cortes = list(precios.keys())
        
        print("\n-------------- Cortes de Carne --------------\n 1 - Lomo 300g - $450\n 2 - Costillas 500g - $1000\n 3 - Res 200g - $400\n 4 - Rib Eye 300g - $550\n 5 - New York 400g - $1000\n-------------- Cortes de Carne -------------\n")
        corte = input("\nSelecciona el corte de carne que te gustaria ordenar: ")

        if corte == "1":
            print(f"\n----- Ordenó un {cortes[0]} + $", precios["Lomo"], "a la cuenta")
            cuenta = cuenta + precios["Lomo"]
        if corte == "2":
            print(f"\n----- Ordenó un {cortes[1]} + $", precios["Costillas"], "a la cuenta")
            cuenta = cuenta + precios["Costillas"]
        if corte == "3":
            print(f"\n----- Ordenó un {cortes[2]} + $", precios["Res"], "a la cuenta")
            cuenta = cuenta + precios["Res"]
        if corte == "4":
            print(f"\n----- Ordenó un {cortes[3]} + $", precios["Rib Eye"], "a la cuenta")
            cuenta = cuenta + precios["Rib Eye"]
        if corte == "5":
            print(f"\n----- Ordenó un {cortes[4]} + $", precios["New York"], "a la cuenta")
            cuenta = cuenta + precios["New York"]
         
    elif modo == "2":
        precios = {"Cangrejo": 450, "Mejillón": 250, "Pulpo": 220, "Langosta": 950, "Salmón":350}
        cortes = list(precios.keys())

        print("\n-------------- Mariscos --------------\n 1 - Cangrejo 200g - $450\n 2 - Mejillón 100g - $250\n 3 - Pulpo 200g - $220\n 4 - Langosta 200g - $950\n 5 - Salmón 200g - $350\n-------------- Marisco -------------\n")
        corte = input("\nSelecciona el marisco que te gustaria ordenar: ")

        if corte == "1":
            print(f"\n----- Ordenó un {cortes[0]} + $", precios["Cangrejo"], "a la cuenta")
            cuenta = cuenta + precios["Cangrejo"]
        if corte == "2":
            print(f"\n----- Ordenó un {cortes[1]} + $", precios["Mejillón"], "a la cuenta")
            cuenta = cuenta + precios["Mejillón"]
        if corte == "3":
            print(f"\n----- Ordenó un {cortes[2]} + $", precios["Pulpo"], "a la cuenta")
            cuenta = cuenta + precios["Pulpo"]
        if corte == "4":
            print(f"\n----- Ordenó un {cortes[3]} + $", precios["Langosta"], "a la cuenta")
            cuenta = cuenta + precios["Langosta"]
        if corte == "5":
            print(f"\n----- Ordenó un {cortes[4]} + $", precios["Salmón"], "a la cuenta")
            cuenta = cuenta + precios["Salmón"]

    elif modo == "3":
        precios = {"Fusilli": 200, "Penne": 180, "Ravioli": 180, "Lasaña": 350, "Alfredo":250}
        cortes = list(precios.keys())

        print("\n-------------- Pastas --------------\n 1 - Fusilli 150g - $200\n 2 - Penne 100g - $180\n 3 - Ravioli 120g - $180\n 4 - Lasaña 200g - $350\n 5 - Alfredo 200g - $250\n-------------- Pastas -------------\n")
        corte = input("\nSelecciona la pasta que te gustaria ordenar: ")

        if corte == "1":
            print(f"\n----- Ordenó un {cortes[0]} + $", precios["Fusilli"], "a la cuenta")
            cuenta = cuenta + precios["Fusilli"]
        if corte == "2":
            print(f"\n----- Ordenó un {cortes[1]} + $", precios["Penne"], "a la cuenta")
            cuenta = cuenta + precios["Penne"]
        if corte == "3":
            print(f"\n----- Ordenó un {cortes[2]} + $", precios["Ravioli"], "a la cuenta")
            cuenta = cuenta + precios["Ravioli"]
        if corte == "4":
            print(f"\n----- Ordenó un {cortes[3]} + $", precios["Lasaña"], "a la cuenta")
            cuenta = cuenta + precios["Lasaña"]
        if corte == "5":
            print(f"\n----- Ordenó un {cortes[4]} + $", precios["Alfredo"], "a la cuenta")
            cuenta = cuenta + precios["Alfredo"]
        
    elif modo == "4":
        precios = {"Refresco": 40, "Jugo de Naranja": 50, "Agua de Jamaica": 40, "Vino": 250, "Cerveza":70}
        cortes = list(precios.keys())

        print("\n-------------- Bebidas --------------\n 1 - Refresco 350ml - $40\n 2 - Jugo de Naranja 200ml - $50\n 3 - Agua de Jamaica 200ml - $40\n 4 - Vino 80ml - $250\n 5 - Cerveza 300ml - $70\n-------------- Bebidas -------------\n")
        corte = input("\nSelecciona la bebida que te gustaria ordenar: ")

        if corte == "1":
            print(f"\n----- Ordenó un {cortes[0]} + $", precios["Refresco"], "a la cuenta")
            cuenta = cuenta + precios["Refresco"]
        if corte == "2":
            print(f"\n----- Ordenó un {cortes[1]} + $", precios["Jugo de Naranja"], "a la cuenta")
            cuenta = cuenta + precios["Jugo de Naranja"]
        if corte == "3":
            print(f"\n----- Ordenó un {cortes[2]} + $", precios["Agua de Jamaica"], "a la cuenta")
            cuenta = cuenta + precios["Agua de Jamaica"]
        if corte == "4":
            print(f"\n----- Ordenó un {cortes[3]} + $", precios["Vino"], "a la cuenta")
            cuenta = cuenta + precios["Vino"]
        if corte == "5":
            print(f"\n----- Ordenó un {cortes[4]} + $", precios["Cerveza"], "a la cuenta")
            cuenta = cuenta + precios["Cerveza"]
        
    elif modo == "5":
        precios = {"Helado de limón": 45, "Flan": 65, "Cheese cake": 95, "Pastel de chocolate": 120, "Ate con queso":90}
        cortes = list(precios.keys())

        print("\n-------------- Postres --------------\n 1 - Helado de limón 70g - $45\n 2 - Flan 100g - $65\n 3 - Cheese cake 150g - $95\n 4 - Pastel de chocolate 90g - $120\n 5 - Ate con queso 70g - $90\n-------------- Postres -------------\n")
        corte = input("\nSelecciona el postre que te gustaria ordenar: ")

        if corte == "1":
            print(f"\n----- Ordenó un {cortes[0]} + $", precios["Helado de limón"], "a la cuenta")
            cuenta = cuenta + precios["Helado de limón"]
        if corte == "2":
            print(f"\n----- Ordenó un {cortes[1]} + $", precios["Flan"], "a la cuenta")
            cuenta = cuenta + precios["Flan"]
        if corte == "3":
            print(f"\n----- Ordenó un {cortes[2]} + $", precios["Cheese cake"], "a la cuenta")
            cuenta = cuenta + precios["Cheese cake"]
        if corte == "4":
            print(f"\n----- Ordenó un {cortes[3]} + $", precios["Pastel de chocolate"], "a la cuenta")
            cuenta = cuenta + precios["Pastel de chocolate"]
        if corte == "5":
            print(f"\n----- Ordenó un {cortes[4]} + $", precios["Ate con queso"], "a la cuenta")
            cuenta = cuenta + precios["Ate con queso"]

    start = input("\nDesea ordenar algo más si/no: ")

    if start == "no":
        print(f"\n--------- Su TOTAL es = ${cuenta} ---------")

        print("\nPuedes pagar con cualquiera de los siguentes bancos \n 1 - BBVA\n 2 - Santander\n 3 - Banco Azteca")
        banco = input("\nSelecciona el banco con el que deseas pagar: ")

        if banco == "1" or banco == bancos[0]:

            print(f"\nAl pagar con BBVA se puede aplicar un descuento del 10% al monto de ${cuenta}")
        
            desc = input("\n¿Deseas aplicarla? si/no: ")

            if desc == "si" or desc == "SI" or desc == "Si":
                porc = cuenta*0.1
                desc_banc = cuenta - porc
                print(f"\n--------- Con el descuento bancario TOTAL a pagar es de ${desc_banc} ---------")
            else:
                cuenta = cuenta

        if banco == "2" or banco == bancos[1]:

            print(f"\nAl pagar con Santander se puede aplicar un descuento del 5% al monto de ${cuenta}")
        
            desc = input("\n¿Deseas aplicarla? si/no: ")

            if desc == "si" or desc == "SI" or desc == "Si":
                porc = cuenta*0.1
                desc_banc = cuenta - porc
                print(f"\n--------- Con el descuento bancario TOTAL a pagar es de ${desc_banc} ---------")
            else:
                cuenta = cuenta

        if banco == "3" or banco == bancos[2]:

            print(f"\nAl pagar con Banco Azteca se puede aplicar un descuento del 12% al monto de ${cuenta}")
        
            desc = input("\n¿Deseas aplicarla? si/no: ")

            if desc == "si" or desc == "SI" or desc == "Si":
                porc = cuenta*0.1
                desc_banc = cuenta - porc
                print(f"\n--------- Con el descuento bancario TOTAL a pagar es de ${desc_banc} ---------")
            else:
                cuenta = cuenta

        if cuenta >= 1500:
            cuenta = cuenta - 200
            cuenta = cuenta - porc
            print("\n-------- FELICIDADES, por tu compra superior a $1500 te llevas un cupón con $200 de regalo -------- ")

        if cuenta < 200:
            cuenta + 30
            print("\n--------- Como su compra es inferior a $200 se le cobraran 30 pesos extra de envío ---------\n")

        print(f"\n-------------- Con el descuento bancario y los cupones canjeados el TOTAL a pagar es de ${cuenta} --------------\n")
    

      



