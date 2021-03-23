# Entrada
nombre = input("¿Cuál es tu nombre?: ")

# Salida
print(f"Me alegro de conocerte {nombre}")

edad = input("¿Cuántos años tienes?: ")
# print(f"el año que viene tendrás {edad + 1} años") #error
print(f"el año que viene tendrás {int(edad) + 1} años")
