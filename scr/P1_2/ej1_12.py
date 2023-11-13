def main():
    kilos = int(input("dime tu peso en kg: "))
    altur = int(input("dime tu altura en centimetros: "))
    indcor = (kilos/(altur/100)**2)
    print("Su indice de masa corporal es de ",indcor)
if __name__ == "__main__":
    main()