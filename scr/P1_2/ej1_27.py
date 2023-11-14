def main():
    print("Dime el nombre del producto, su precio y el numero de unidades")
    NomProd = input("Nombre: ")
    Precio = float(input("Precio: "))
    NumeUnid = int(input("Numero de unidades: "))
    costetotal = Precio * NumeUnid
    
    print("{}-{:6.2f}-{:3d}-{:8.2f}".format(NomProd,Precio,NumeUnid,costetotal))
    print("nombre-precio-NumeroUnidades-Costetotal")

if __name__ == "__main__":
    main()