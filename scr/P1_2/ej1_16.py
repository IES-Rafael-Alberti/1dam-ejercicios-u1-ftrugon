def main():
    numbarraspochas = int(input("Cuantas barras pochas se han vendido? "))
    preciobarrasbuenas = 3.49
    print("Una barra fresca cuesta: " + str(preciobarrasbuenas))
    dinerobarraspochas = (numbarraspochas * preciobarrasbuenas) * 0.6
    print(f"Se han vendido {round(dinerobarraspochas,2)}€ de barras pochas")
if __name__ == "__main__":
    main()
