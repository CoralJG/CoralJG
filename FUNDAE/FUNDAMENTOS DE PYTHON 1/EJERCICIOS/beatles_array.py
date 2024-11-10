beatles = []
# paso 1
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 1:", beatles)

# paso 2
for i in range(2):
    user_input = str(input("Agrega más miembros de la banda: "))
    beatles.append(user_input)
    continue
print("Paso 2:", beatles)

# paso 3
del beatles[4]
del beatles[3] 
print("Paso 3:", beatles)

# paso 4
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
