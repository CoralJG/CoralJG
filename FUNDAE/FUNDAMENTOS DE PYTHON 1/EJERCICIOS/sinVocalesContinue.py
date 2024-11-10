# Variable para almacenar la palabra sin vocales
word_without_vowels = ""

# Indicar al usuario que ingrese una palabra y asignarla a la variable user_word
user_word = input("Escribe una palabra: ")

# Recorrer cada letra en la palabra ingresada por el usuario
for letter in user_word:
    # Verificar si la letra es una vocal
    if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
        continue  # Saltar las vocales
    else:
        # Agregar la consonante a word_without_vowels
        word_without_vowels += letter

# Imprimir la palabra sin vocales
print("Palabra sin vocales:", word_without_vowels)
