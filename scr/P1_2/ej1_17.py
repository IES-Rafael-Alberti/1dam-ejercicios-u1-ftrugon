def main():
    nombre = input("dime tu nombre: ")
    cilos = int(input("cuantas veces quiere que se repita? "))
    while cilos > 0:
        print(nombre)
        cilos = cilos - 1
if __name__ == "__main__":
    main()