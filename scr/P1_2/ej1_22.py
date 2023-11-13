def main():
    frase = input("Dame una frase: ")
    vocal = input("Ahora una vocal en minusculas: ")
    frase = frase.replace(vocal.lower(),vocal.upper())
    
    print(f"{frase}")
    
if __name__ == "__main__":
    main()