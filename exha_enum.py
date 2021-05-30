def run():
    square_root = int(input("Ingrese un número para calcular su raíz cuadrada: "))
    square = 0

    while square**2 < square_root:
        square += 1

    if square**2 == square_root:
        print ("La raíz cuadrada de", square_root, "es", square)
    else:
        print (square_root, "no tiene raíz cuadrada exacta")

if __name__ == "__main__":
    run()