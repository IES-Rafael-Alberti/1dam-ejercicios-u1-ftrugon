def main():
    inicio = int(input("Dime un inicio: "))

    incremento = int(input("Dime un incremento: "))

    while incremento < 0:
        print("El incremento tiene que ser mayor a 0")
        incremento = int(input("Dame de nuevo el numero: "))

    totalserie = int(input("Dime un total de serie:"))

    while totalserie < 0:
        print("El incremento tiene que ser mayor a 0")
        incremento = int(input("Dame de nuevo el numero: "))
        
    serie = str("serie=> "+str(inicio))
    while inicio < totalserie:
        inicio += incremento
        serie = serie + "-" + str(inicio) 
    else:
        print(serie)


if __name__ == "__main__":
    main()