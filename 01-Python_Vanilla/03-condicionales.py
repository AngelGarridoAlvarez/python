# CONDICIONALES if, else, elif

color = input("¿de qué color está el semáforo?: ")

if color == "rojo":
    print("No puedes cruzar el semáforo")
elif color == "verde":
    print("Puedes cruzar tranquilo")
elif color == "amarillo":
    print("Puedes cruzar corriendo")
else:
    print("el semáforo no tiene ese color")

""" 
OPERADORES LOGICOS

and
or
! (negación)
not

"""
edad = input("¿Cuantos años tienes?: ")
print(edad)
carnet = input("¿Tienes carnet de conducir? responde si o no: ")
print(carnet)

if int(edad) >= 18 and carnet == "si":
    print("Puedes conducir!")
else:
    print("no puedes conducir")

