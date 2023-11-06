def main():
    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))
    if num1 > num2:
        inicio = num2
        final = num1
    else:
        inicio = num1
        final = num2
    linea = str(inicio)
    while inicio <= final:
        inicio = inicio + 1
        linea = linea + "-" + str(inicio)
        if inicio == final:
            print(linea)
        
if __name__ == "__main__":
    main()