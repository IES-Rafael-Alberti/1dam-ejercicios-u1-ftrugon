def main():
    num1 = int(input("Dime un numero:  "))
    num2 = int(input("Dime otro numero: "))
    print("Pon 1 de las 4 opciones (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División)")
    op = int(input("Que operacion quieres hacer? "))
    while op > 4 or op < 1:
        print("No es una opcion valida")
        print("Pon 1 de las 4 opciones (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División)")
        op = int(input("Que operacion quieres hacer? "))

    if op == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    if op == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    if op == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    if op == 4:
        if num2 == 0:
            print(f"No puedes dividir {num1} galletas entre 0 amigos")
        else:
            print(f"{num1} / {num2} = {num1/num2}")
if __name__ == "__main__":
    main()