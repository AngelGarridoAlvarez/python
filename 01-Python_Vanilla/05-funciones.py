#la buena práctica es que las funciones devuelvan return y que luego hagamos el print

# Función sin parámetros
def muestraNombre():
    print(f"el nombre es Angel")
    print(f"el nombre es Pepe")
    print(f"el nombre es Manuel")
    print(f"el nombre es Raúl")
    print(f"el nombre es Didi")

muestraNombre()


# Función con paramétros obligatorios
def muestraNombre2(nombre):
    print(f"el nombre es {nombre}")

muestraNombre2("Supercalifragilísticoespialidoso")

# Función con parámetros opcionales

def muestraNombre3(nombre, apellido = "Sin Apellido"):
    print (f"el nombre completo es {nombre} {apellido}.")

muestraNombre3("Ángel")
muestraNombre3("Ángel", "Garrido")

# Función con return

def funcionSuma(num1 = 0, num2 = 0):
    return num1 + num2


print(funcionSuma(1,2))
print(4 + funcionSuma(1))
print(4 + funcionSuma(1,2))

# FUNCIONES LAMBDA (Equivalente a funciones flecha de JS)
# Es una función anónima, no hace falta definirla, sirven para tareas simples y repetitivas, se definen en una sola línea

dime_el_year = lambda year: f"El año es {year}"
print(dime_el_year(1925))

# FUNCIONES PREDEFINIDAS
print("Print es una función predefinida")
print(type("Type es una función predefinida que te dice el tipo"))

x = isinstance(5, int)
print(x) #true
"""
The isinstance() function returns True if the specified object is of the specified type, otherwise False.

If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
"""

# .strip() Quitar espacios la terales

frase = "   Este texto tiene espacios a los lados   "
print(frase)
print(frase.strip())

#del - borrar varialble

year = 2012
del year 
#print(year) #NameError: name 'year' is not defined

#lent() tamaño del string

texto = "Hello"

print(len(texto)) # 5

#.repalce

frase = "La vida es bellisima"
newFrase = frase.replace("vida","moto")
print(frase) #La vida es bellisima
print(newFrase) #La moto es bellisima

# .upper() .lower()
print(newFrase.upper()) #LA MOTO ES BELLISIMA