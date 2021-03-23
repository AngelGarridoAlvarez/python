"""
SET es un tipo de dato, para tener una colección de valores, pero no tiene ni indice ni orden
* Mejor usar listas
"""

personas = {
    "Víctor",
    "Ángel",
    "Francisca"
}

print(personas) #{'Francisca', 'Ángel', 'Víctor'}

personas.add("Paco")
print(personas) #{'Francisca', 'Víctor', 'Ángel', 'Paco'} lo ordena aleatoriamente

personas.remove("Víctor")
print(personas) #{'Ángel', 'Paco', 'Francisca'}


# Diccionarios: simlar los JSON, almacena una clave y un valor

persona = {
    "nombre": "Ángel",
    "apellidos": "Garrido Álvarez",
    "web": "https://angeldeveloper.es"
}

print(persona) #{'nombre': 'Ángel', 'apellidos': 'Garrido Álvarez', 'web': 'https://angeldeveloper.es'}

print(persona["apellidos"]) #Garrido Álvarez


# Diccionarios dentro de listas

videojuegos = [
    {
        'juego':'Super Mario Galaxy',
        'consola':'Wii',
        'año': 2008
    },
     {
        'juego':'Starfox Adventures',
        'consola':'Gamecube',
        'año': 2003
    },
     {
        'juego':'The Legend of Zelda Ocarina of Time',
        'consola':'Nintendo 64',
        'año': 1998
    }
]

print(videojuegos[0]) # {'Juego': 'Super Mario Galaxy', 'Consola': 'Wii', 'año': 2008}
print(videojuegos[2]["consola"]) # Nintendo 64
print(videojuegos[2]["juego"]) # The Legend of Zelda Ocarina of Time
print("\n Lista de auperconsolas míticas:")

contador = 0

for videojuego in videojuegos:
    contador += 1
    print(f"{contador}. {videojuego['consola']}")
    
"""
1. Wii
2. Gamecube
3. Nintendo 64
"""