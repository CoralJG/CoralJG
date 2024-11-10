# Leer un número natural ingresado por el usuario
c0 = int(input("Ingresa un número natural: "))

# Verificar que el número ingresado es positivo
if c0 < 1:
    print("Por favor ingresa un número natural mayor que 0.")
else:
    # Inicializar el contador de pasos
    steps = 0

    # Bucle para aplicar la secuencia de Collatz hasta que c0 llegue a 1
    while c0 != 1:
        print(c0)  # Imprimir el valor actual de c0

        # Aplicar la operación según si c0 es par o impar
        if c0 % 2 == 0:
            c0 //= 2  # Si es par, dividir entre 2
        else:
            c0 = 3 * c0 + 1  # Si es impar, calcular 3*c0 + 1

        steps += 1  # Incrementar el contador de pasos

    # Imprimir el último valor (1) y la cantidad de pasos
    print(c0)
    print("pasos =", steps)
