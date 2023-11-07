def main():
    nombre = input("Dime tu nombre: ")
    if nombre == "":
        print("Desconocido")
    else:
        edad = int(input("Ahora dime tu edad"))
        if edad < 0 or edad > 125:
            print("Error en la edad: ")
        else:
            edad2 = edad - 125
            print(f"Eres {nombre}, tienes {edad} años y te quedan {abs(edad2)} años")
    
if __name__ == "__main__":
    main()