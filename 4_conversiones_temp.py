
print("\n--- Este es un conversor automatico entre escalas de medida de temperatura ---\n----- 'Escalas de temperatura:'\t\t'celsius = c'\t\t'fahrenheit = f'\t'kelvin = k' -----\n--- Ejemplo : cf = celcius a fahrenheit (La inicial de la primera escala y la inicial de la segunda) ---\n ")

def check(variable):
    global out 
    while type(variable) == str:
        try:
            variable = float(variable)
            out = variable
        except:
            if type(variable) == str:
                variable = input("Digite un valor numérico: ")

def oper (variable,rest,mult,div,sum):
    global resault
    resault = ((((variable-rest)*mult)/div)+sum)

start  = str(input("Presione 's' para iniciar: "))
temp  = ["cf","ck","fc","fk","kc","kf"]
cont_1 = 0# Contador para ver el número de veces que pone una escala mal
cont_2 = 1# Contador para el multiplicador y volver a mostrar las escalas cada 5 intentos


while start == "s" or start == "S":
    start = start+"."
    scales = str(input("\f---Digite la escala que posee y a la que quiere convertir: "))

    while scales not in temp:
        cont_1 = cont_1  + 1
        scales = str(input("---Por favor digite escalas válidas: "))

        if cont_1 == 4*cont_2:
           cont_2  = cont_2 + 1
           print("\f-----Escalas de temperatura\t\t'celsius = c'\t\t'fahrenheit = f'\t'kelvin = k'-----\n\tEjemplo : cf = celcius a fahrenheit (La inicial de la primera escala y la inicial de la segunda)\n")
           scales = str(input("---Por favor digite temperaturas válidas: "))
    
  
    if scales == "cf":
        cels_fahr = input("\fDigite los grados celcuius: ")
        check(cels_fahr)

        oper(out,0,1.8,1,32)# Formula F = (C x 1.8) + 32

        print(f"\f\t----{out}°C = {resault}°F ----\n") 

    if scales == "ck":
        cels_kelv = input("\fDigite los grados celcius: ")
        check(cels_kelv)

        oper(out,0,1,1,273.15) # Formula K = C + 273.15

        print("\f\t----",(out),"°C =",(resault),"K ----\n") 

    if scales == "fc":
        fahr_cels = input("\fDigite los grado fahrenheit: ")
        check(fahr_cels)

        oper(out,32,1,1.8,0)# Formula C = (F - 32) / 1.8

        print("\f\t----",(out),"°F =",(resault),"°C ----\n") 
   
    if scales == "fk":
        fahr_kelv = (input("\fDigite los grados fahrenheit: "))
        check(fahr_kelv)

        oper(out,32,1,1.8,273.15)# Formula K = (F -32)/1.8 + 273.15

        print("\f\t----",(out),"°F =",(resault),"K ----\n")

    if scales == "kc":
        kelv_cels = (input("\fDigite los Kelvin: "))
        check(kelv_cels)

        oper(out,273.15,1,1,0)# Formula C = K - 273.15

        print("\f\t----",(out),"K =",(resault),"°C ----\n")
   
    if scales == "kf":
        kelv_fahr =  (input("\fDigite los Kelvin: "))
        check(kelv_fahr)

        oper(out,273.15,1.8,1,32)# Formula F = ((K - 273.15) x 1.8) -32

        print("\f\t----",(out),"K =",(resault),"°F ----\n")

    start = str(input("Desea hacer otra converción s/n: "))
    if start == "n":
        exit()
    while start != "s":
        start = str(input("Por favor digie s/n: "))
        if start == "n":
            exit()