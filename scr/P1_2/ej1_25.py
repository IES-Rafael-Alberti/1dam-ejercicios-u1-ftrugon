def main():
    fecha = input("dime tu fecha de nacimiento(dd/mm/aaaa): ")
    fecha2 = fecha.split("/")
    print(f"naciste es dia {fecha2[0]} del mes {fecha2[1]} del año {fecha2[2]}")
if __name__ == "__main__":
    main()