# Esto es un comentario en python

print("####################################")
print("Hello World! I'm Ángel Developer")
print("####################################")
print(33 + 1)

"""
Esto
es
un
comentario
multilinea
"""

# VARIABLES

texto = "Ángel es la caña"
numero = 45
decimal = 11.2

print(texto)

# no me hace falta cerrar cada línea con ;
"""
No hace falta tipar la variable
nombre = contenido
"""

numero = 123456

# CONCATENACIÓN

print(texto + ", y lo sabes!")

print(f"{texto} y su número es {numero}")

textoConcatenado = f"Vas a ser el rey de Python, tu número es {decimal} y {texto}" #Vas a ser el rey de Python, tu número es 11.2 y Ángel es la caña

print(textoConcatenado)

# Concatenación con método format
nombre = "Ángel"
apellidos = "Garrido Álvarez"
web = "https://www.angeldeveloper.es"
print("Hola me llamo {} {} y mi web es {}".format(nombre, apellidos, web))

# TIPOS DE DATOS

nada = None
cadena = "https://angeldeveloper.es"
entero = 99
flotante = 99.2
booleano = True
lista = [2,4,5]
lista2 = [2,4,5, nada]
tupla = (2,4,5) #en la tupla los datos no cambian
diccionario = { #Es una especie de json que permite tener clave y valor
    "nombre": "Ángel",
    "apellido":"Garrido",
    "web": web
}

rango = range(9) # secuencia numérica del 0 al 9
rango2 = range(4,9) # secuencia numérica del 4 al 9
dato_byte = b"Esto es un dato byte"


print(type(nada)) # <class 'NoneType'>
print(type(cadena)) #<class 'str'>
print(type(entero)) #<class 'int'>
print(type(flotante)) #<class 'float'>
print(type(booleano)) #<class 'bool'>
print(type(lista)) #<class 'list'>
print(lista2) #[2, 4, 5, None]
print(type(flotante)) #<class 'float'>
print(type(tupla)) #<class 'tuple'>
print(type(diccionario))  #<class 'dict'>
print((diccionario))  #{'nombre': 'Ángel', 'apellido': 'Garrido', 'web': 'https://www.angeldeveloper.es'}
print(rango) #range(0, 9)
print(rango2) #range(4, 9)
print(type(rango)) #<class 'range'>
print(type(dato_byte)) #<class 'bytes'>

# CONVERTIR TIPOS DE DATOS

miTexto = "Hello, I'm a text"
numerito = 33
#print(miTexto + numerito) # TypeError: can only concatenate str (not "int") to str
print (miTexto +str(numerito)) #Hello, I'm a text33

# MOSTRAR TEXTOS ENTRECOMILLADOS
print("Usamos \ para usar las \"comillas dentro de comillas\" ") #Usamos \ para usar las "comillas dentro de comillas"
otroTexto = 'Hola "Maricarmen"'

print(otroTexto) #Hola "Maricarmen"

# SALTO DE LINEA \n
byebye = "Hasta luego \nMaricarmen"
print(byebye)
"""
Hasta luego
Maricarmen
"""

# TABULACIÓN \t

byebye = "Hasta luego \tMaricarmen"
print(byebye)
"""
Hasta luego     Maricarmen
"""

# OPERADORES ARITMÉTICOS

numero1 = 77
numero2 = 44

resta = numero1 - numero2
suma = numero1 + numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2

print(f"numero1 = {numero1}\nnumero2 = {numero2}\nsuma + = {suma}\nresta - = {resta}\nmultiplicacion * = {multiplicacion}\ndivision / = {division}\nresto % = {resto}")

# OPERADORES DE ASIGNACIÓN

edad = 55
print(edad) #55
edad += 5
print(edad) #60

#edad ++ no es valido en python