def main():
    TOTnotas =int(input("Cuantas notas vas a introducir: "))

    while TOTnotas < 1 or TOTnotas > 100:
        print("Error - el numero debe ser de 1 a 100")
        TOTnotas =int(input("Cuantas notas vas a introducir: "))

    print(f"Dame las {TOTnotas} notas del curso")

    media = float(0)
    cont = 1
    while cont <= TOTnotas:
        nota = float(input("Dame 1 nota: "))
        if nota > 10:
            print("Una nota de mas de 10 puntos?")
            nota = float(input("Dame 1 nota: "))
        media += nota
        cont += 1

    print(f"La media de notas es {media / TOTnotas}")
if __name__ == "__main__":
    main()