def main():
    prec = input("Pon el precio con 2 decimales: ")
    prec2 = prec.split(".")
    #prec3 = prec2[0]
    #prec4 = prec2[1]
    #print(f"Tu producto cuesta {prec3}€ y {prec4} centimos")
    print(f"Tu producto cuesta {prec2[0]}€ y {prec2[1]} centimos")
if __name__ == "__main__":
    main()