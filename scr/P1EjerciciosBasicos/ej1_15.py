
def main():
    ingresado = int(input("Introduce cuanto vas a ingresar en la cuenta: "))
    año1 = (ingresado * 0.04) + ingresado
    año2 = (año1 * 0.04) + año1
    año3 = (año2 * 0.04) + año2
    print("El interes en el primer año sera de " + str(año1)+ " ,el interes en el primer año sera de " + str(año2) +" y el interes en el primer año sera de " + str(año3))

if __name__ == "__main__":
    main()
