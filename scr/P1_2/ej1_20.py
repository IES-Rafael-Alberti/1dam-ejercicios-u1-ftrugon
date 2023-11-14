def main():
    print(" Recuerda que el formato es +XX-XXXXXXXXX-XX")
    prefijo = input("Dime el numero de telefono: ") 
    numero = prefijo.split("-")
    print("El numero ingresado es: "+numero[1])
    
if __name__ == "__main__":
    main()