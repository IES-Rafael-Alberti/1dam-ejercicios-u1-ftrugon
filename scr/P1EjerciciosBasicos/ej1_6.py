def main():
    Importefinal = int(input("Cual a sido el importe final del articulo: "))
    ivapagado = Importefinal*10/100
    Articulosiniva = Importefinal - ivapagado
    print(Articulosiniva)

if __name__ == "__main__":
    main()