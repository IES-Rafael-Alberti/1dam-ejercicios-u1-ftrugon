def main():
    HT = int(input("horas de trabajo: "))
    CH = int(input("Coste de horas: "))
    IT = HT*CH
    print("Este es el importe total "+ str(IT) + "€")

if __name__ == "__main__":
    main()