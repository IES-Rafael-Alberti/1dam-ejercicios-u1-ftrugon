def main():
    
    print("Dime un numero: ")
    num = int(input("El numero: "))
    while num < 1 or num >10:
        print("incorrecto, escribelo otra vez")
        num = int(input("Intentalo otra vez: "))
    else:
        print("CORRECTO GANASTE :DDDDDD")

if __name__ == "__main__":
    main()