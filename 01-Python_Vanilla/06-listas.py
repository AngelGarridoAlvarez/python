#Listas: es como los Arrays

peliculas = ["Jurassic Park", 33, "Golden Eye" "Terminator 2", "Matrix"]
print(peliculas[0]) # Jurassic Park
peliculas[0] = "El Hobbit"
print(peliculas[0]) # El hobbit

#Con el método list:

peliculas2 = list(("Jurassic Park", 33, "Golden Eye" "Terminator 2", "Matrix"))
print(peliculas2[1]) # 33
peliculas2[1] = 44
print(peliculas2[1]) # 33

# Pasar un rango

numeros = list(range(1,11)) 
print(numeros) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[-2]) #9
print(numeros[0:3]) #[1, 2, 3]
print(numeros[5:]) #[6, 7, 8, 9, 10]

# Añadir elementos a lista

peliculas.append("Encuentros en la tercera fase")
peliculas2.append("Tarzán")
print(peliculas) # ['El Hobbit', 33, 'Golden EyeTerminator 2', 'Matrix', 'Encuentros en la tercera fase']
print(peliculas2) # ['Jurassic Park', 44, 'Golden EyeTerminator 2', 'Matrix', 'Tarzán']

print("\n############# RECORRER LISTAS CON FOR IN ########################\n")
# Recorrer lista con for

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")
"""
############# RECORRER LISTAS CON FOR IN ########################
1. El Hobbit
2. 33
3. Golden EyeTerminator 2
4. Matrix
5. Encuentros en la tercera fase
"""

# LISTAS MULTIDIMENSIONALES
# Son listas dentro de otras listas
print("\n############# Listas Multidimensionales ########################\n")

contactos = [
    [
        'Salvador Illa',
        'salvador@ministroilla.com'
    ],
      [
        'Ángel Garrido',
        'contacto@angeldeveloper.es'
    ]
]

print(contactos)
print("\n" + contactos[1][1])



for contacto in contactos:
    print(contacto)

"""
['Salvador Illa', 'salvador@ministroilla.com']
['Ángel Garrido', 'contacto@angeldeveloper.es']
"""

print("\n")

# Sacamos solo los nombres


for contacto in contactos:
    print(contacto[0])


"""
Salvador Illa
Ángel Garrido
"""

print("\n")

# Anidamos un for dentro de otro for para sacar cada elemento de la sublista

for contacto in contactos:
    for elemento in contacto:
        print(elemento)

"""
Salvador Illa
salvador@ministroilla.com
Ángel Garrido
contacto@angeldeveloper.es

"""

## FUNCIONES Y MÉTODOS PREDEFINID@S PARA TRABAJAR CON LISTAS

cantantes = ["Julio Iglesias", "Fito", "Roxana", "Eminem", "Carlos Baute", "Freddy Mercury"]
numeritos = [22, 33, 55, 2342, 1, 18, 254, 4, 74, 36]

print(numeritos)
print(cantantes)

#Ordenar
numeritos.sort()
print(numeritos)
cantantes.sort()
print(cantantes)
"""
[22, 33, 55, 2342, 1, 18, 254, 4, 74, 36]
[1, 4, 18, 22, 33, 36, 55, 74, 254, 2342]
"""
# Añadir elementos
cantantes.insert(0,"Michael Jackson")
print(cantantes) #['Michael Jackson', 'Carlos Baute', 'Eminem', 'Fito', 'Freddy Mercury', 'Julio Iglesias', 'Roxana']

# Eliminar elementos
cantantes.pop()
print(cantantes) #['Michael Jackson', 'Carlos Baute', 'Eminem', 'Fito', 'Freddy Mercury', 'Julio Iglesias']
cantantes.pop(0)
print(cantantes)  #['Carlos Baute', 'Eminem', 'Fito', 'Freddy Mercury', 'Julio Iglesias']
cantantes.remove('Fito')
print(cantantes)  #['Carlos Baute', 'Eminem', 'Freddy Mercury', 'Julio Iglesias']

#dar la vuelta
cantantes.reverse() #['Julio Iglesias', 'Freddy Mercury', 'Eminem', 'Carlos Baute']

#Buscar en una lista
print('Carlos Baute' in cantantes) #True

# Contar elementos dentro de una lista
print(len(cantantes))

# Cuántas veces aparece un elemento en una lista
print(numeritos.count(55)) #0

# Conseguir indice
print((cantantes.index("Eminem"))) #2

# Unir Listas
cantantes.extend(numeritos)
print(cantantes) #['Julio Iglesias', 'Freddy Mercury', 'Eminem', 'Carlos Baute', 1, 4, 18, 22, 33, 36, 55, 74, 254, 2342]