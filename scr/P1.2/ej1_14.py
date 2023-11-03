def main():
    PPayaso = int(112)
    PMuñeca = int(75)
    Npayaso = int(input("Cuantos payasos se han vendido: "))
    Nmuñeca = int(input("Cuantas muñecas se han vendido: "))
    print("Todo el cargamento es de "+str(((PPayaso * Npayaso) + (PMuñeca * Nmuñeca))/100)+ "kg")
if __name__ == "__main__":
    main()