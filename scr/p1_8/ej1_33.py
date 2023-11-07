def main():
    print("Dame 3 numeros:")
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    n3 = int(input("numero 3: "))
    if n1 == min(n1,n2,n3):
        if n2 < n3:
            print(f"El orden de los numeros es {n1} {n2} {n3}")
        else:
            print(f"El orden de los numeros es {n1} {n3} {n2}")
    elif n2 == min(n1,n2,n3):
        if n1 < n3:
            print(f"El orden de los numeros es {n2} {n1} {n3}")
        else:
            print(f"El orden de los numeros es {n2} {n3} {n1}")
    else:
        if n1 < n2:
            print(f"El orden de los numeros es {n3} {n1} {n2}")
        else:
            print(f"El orden de los numeros es {n3} {n2} {n1}")
if __name__ == "__main__":
    main()