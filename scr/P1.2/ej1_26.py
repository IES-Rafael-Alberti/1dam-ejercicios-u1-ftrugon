def main():
    cesta = input("Dime tu cesta de la compra separada por comas: ")
    cesta = cesta.split(",")
    print ("\n" .join(cesta))
if __name__ == "__main__":
    main()