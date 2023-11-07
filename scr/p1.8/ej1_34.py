def main():
    serie = int(input("De cuantos numeros va a ser la serie: "))
    num = 3
    cont = 1
    linea = str(num)    
    while cont <= serie:
        cont += 1
        num += 3
        linea += " " + str(num)
        if cont == serie:
            print(linea)

if __name__ == "__main__":
    main()