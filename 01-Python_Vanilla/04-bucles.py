# BUCLE FOR

for contador in range(0, 5):
    print("voy por el número " + str(contador))

# BUCLE WHILE

contador = 0


while contador <= 10:
    contador += 1
    print("Ahora voy por el " + str(contador))

# BUCLE con else
while contador <= 15:
    contador += 1
    print("Ahora MISMO voy por el " + str(contador))
else:
    print("Se ha superado el número máximo")

# BREAK

while contador <= 20:
    contador += 1
    print("Ahora MISMO voy por el " + str(contador))
    if contador == 19:
        print("interrumpo el bucle while utilizando break")
        break